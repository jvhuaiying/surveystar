from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from sqlmodel import Session, select

from database import AiModel, engine


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


def get_ai_models() -> Sequence[AiModel]:
    with Session(engine) as session:
        statement = select(AiModel)
        return session.exec(statement).all()
