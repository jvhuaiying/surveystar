from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ai_model.schemas import (
    CreateAiModelRequestSchemas,
    GetAiModelResponseSchemas,
    MessageResponseSchemas,
)
from ai_model.services import create_ai_model, get_ai_model_by_name, get_ai_models
from auth import get_current_admin
from database import Account

router = APIRouter(prefix="/ai-model", tags=["AI模型管理"])


@router.post("/", response_model=MessageResponseSchemas)
def create_ai_model_router(
    data: CreateAiModelRequestSchemas,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    if get_ai_model_by_name(data.name) is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="模型名称已存在！")
    create_ai_model(
        name=data.name,
        api_key=data.api_key,
        base_url=data.base_url,
        is_active=data.is_active,
        model_type=data.model_type,
        provider_id=data.provider_id,
    )
    return MessageResponseSchemas(detail="模型创建成功！")


@router.get("/", response_model=list[GetAiModelResponseSchemas])
def get_ai_models_router(
    admin: Annotated[Account, Depends(get_current_admin)],
) -> list[GetAiModelResponseSchemas]:
    models = get_ai_models()
    return [
        GetAiModelResponseSchemas(
            id=str(i.id),
            name=i.name,
            api_key=i.api_key,
            base_url=i.base_url,
            is_active=i.is_active,
            model_type=i.model_type,
            provider_id=str(i.provider_id),
            created_at=i.created_at,
            updated_at=i.updated_at,
        )
        for i in models
    ]
