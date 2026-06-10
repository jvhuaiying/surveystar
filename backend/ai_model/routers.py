from datetime import datetime, timezone
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from ai_model.schemas import (
    CreateAiProviderRequestSchemas,
    GetAiProviderResponseSchemas,
    MessageResponseSchemas,
    UpdateAiProviderRequestSchemas,
)
from ai_model.services import (
    create_ai_provider,
    get_ai_provider_by_id,
    get_ai_provider_by_name,
    get_ai_providers,
    update_ai_provider,
    update_ai_provider_status,
)
from auth import get_current_admin
from database import Account

router = APIRouter(prefix="/ai-model", tags=["AI模型管理"])


@router.post("/provider/", response_model=MessageResponseSchemas)
def create_ai_provider_router(
    data: CreateAiProviderRequestSchemas,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    if get_ai_provider_by_name(data.name) is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="提供商名称已存在！")
    now = datetime.now(timezone.utc)
    create_ai_provider(
        name=data.name,
        is_active=data.is_active,
        created_at=now,
        updated_at=now,
    )
    return MessageResponseSchemas(detail="提供商创建成功！")


@router.get("/provider/", response_model=list[GetAiProviderResponseSchemas])
def get_ai_providers_router(
    admin: Annotated[Account, Depends(get_current_admin)],
) -> list[GetAiProviderResponseSchemas]:
    providers = get_ai_providers()
    return [
        GetAiProviderResponseSchemas(
            id=str(i.id),
            name=i.name,
            is_active=i.is_active,
            created_at=i.created_at,
            updated_at=i.updated_at,
        )
        for i in providers
    ]


@router.patch("/provider/{id}/disable", response_model=MessageResponseSchemas)
def disable_ai_provider_router(
    id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    provider = get_ai_provider_by_id(id)
    if provider is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="提供商不存在！")
    update_ai_provider_status(provider, False)
    return MessageResponseSchemas(detail="提供商已禁用！")


@router.patch("/provider/{id}/activate", response_model=MessageResponseSchemas)
def activate_ai_provider_router(
    id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    provider = get_ai_provider_by_id(id)
    if provider is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="提供商不存在！")
    update_ai_provider_status(provider, True)
    return MessageResponseSchemas(detail="提供商已启用！")


@router.get("/provider/{id}", response_model=GetAiProviderResponseSchemas)
def get_ai_provider_by_id_router(
    id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> GetAiProviderResponseSchemas:
    provider = get_ai_provider_by_id(id)
    if provider is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="提供商不存在！")
    return GetAiProviderResponseSchemas(
        id=str(provider.id),
        name=provider.name,
        is_active=provider.is_active,
        created_at=provider.created_at,
        updated_at=provider.updated_at,
    )


@router.patch("/provider/{id}", response_model=MessageResponseSchemas)
def update_ai_provider_router(
    id: UUID,
    data: UpdateAiProviderRequestSchemas,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    provider = get_ai_provider_by_id(id)
    if provider is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="提供商不存在！")
    existing = get_ai_provider_by_name(data.name)
    if existing is not None and existing.id != id:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="提供商名称已存在！")
    update_ai_provider(provider, data.name, data.is_active)
    return MessageResponseSchemas(detail="提供商修改成功！")
