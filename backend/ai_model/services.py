from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from openai import (
    APIError,
    APIConnectionError,
    APIResponseValidationError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    OpenAI,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from sqlmodel import Session, select

from database import AiModel, engine
from enums.ai_model import AiModelTestStatus


def create_ai_model(
    name: str,
    api_key: str,
    base_url: str,
    is_active: bool,
    model_type: str,
    provider_id: UUID,
):
    now = datetime.now(timezone.utc)
    ai_model = AiModel(
        name=name,
        api_key=api_key,
        base_url=base_url,
        is_active=is_active,
        model_type=model_type,
        test_status=AiModelTestStatus.untested,
        provider_id=provider_id,
        created_at=now,
        updated_at=now,
    )
    with Session(engine) as session:
        session.add(ai_model)
        session.commit()
        session.refresh(ai_model)


def get_ai_model_by_name(name: str) -> AiModel | None:
    with Session(engine) as session:
        statement = select(AiModel).where(AiModel.name == name)
        return session.exec(statement).first()


def get_ai_model_by_id(model_id: UUID) -> AiModel | None:
    with Session(engine) as session:
        statement = select(AiModel).where(AiModel.id == model_id)
        return session.exec(statement).first()


def get_ai_models() -> Sequence[AiModel]:
    with Session(engine) as session:
        statement = select(AiModel)
        return session.exec(statement).all()


def test_ai_model(ai_model: AiModel) -> dict:
    try:
        client = OpenAI(base_url=ai_model.base_url, api_key=ai_model.api_key)
        client.models.retrieve(model=ai_model.name)
        ai_model.test_status = AiModelTestStatus.success
        return {"status": True, "message": None}
    except AuthenticationError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"身份认证失败，请检查 API Key：{e}"}
    except APIConnectionError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"无法连接到 API 地址 {ai_model.base_url}：{e}"}
    except APITimeoutError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"连接超时：{e}"}
    except RateLimitError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"请求频率超限：{e}"}
    except PermissionDeniedError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"权限不足：{e}"}
    except NotFoundError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"模型 {ai_model.model_type} 不存在：{e}"}
    except BadRequestError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"请求参数错误：{e}"}
    except ConflictError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"资源冲突：{e}"}
    except UnprocessableEntityError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"请求语义错误：{e}"}
    except InternalServerError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"服务端内部错误：{e}"}
    except APIResponseValidationError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"API 响应格式异常：{e}"}
    except APIError as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"API 请求失败：{e}"}
    except Exception as e:
        ai_model.test_status = AiModelTestStatus.failed
        return {"status": False, "message": f"未知错误：{e}"}
    finally:
        ai_model.updated_at = datetime.now(timezone.utc)
        with Session(engine) as session:
            session.add(ai_model)
            session.commit()
            session.refresh(ai_model)
