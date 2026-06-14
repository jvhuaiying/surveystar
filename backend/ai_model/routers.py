from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from ai_model.schemas import (
    CreateAiModelRequestSchemas,
    GetAiModelResponseSchemas,
    MessageResponseSchemas,
    UpdateAiModelRequestSchemas,
)
from ai_model.services import (
    create_ai_model,
    delete_ai_model,
    get_ai_model_by_id,
    get_ai_model_by_name,
    get_ai_models,
    test_ai_model,
    update_ai_model,
)
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
            test_status=i.test_status,
            provider_id=str(i.provider_id),
        )
        for i in models
    ]


@router.get("/{model_id}/test", response_model=MessageResponseSchemas)
def test_ai_model_router(
    model_id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    model = get_ai_model_by_id(model_id)
    if model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="模型不存在！")
    result = test_ai_model(model)
    if not result["status"]:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=result["message"])
    return MessageResponseSchemas(detail="模型测试成功！")


@router.patch("/{model_id}", response_model=MessageResponseSchemas)
def update_ai_model_router(
    model_id: UUID,
    data: UpdateAiModelRequestSchemas,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    model = get_ai_model_by_id(model_id)
    if model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="模型不存在！")
    existing = get_ai_model_by_name(data.name)
    if existing is not None and existing.id != model_id:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="模型名称已存在！")
    update_ai_model(
        model,
        name=data.name,
        api_key=data.api_key,
        base_url=data.base_url,
        is_active=data.is_active,
        model_type=data.model_type,
        provider_id=data.provider_id,
    )
    return MessageResponseSchemas(detail="模型修改成功！")


@router.get("/{model_id}", response_model=GetAiModelResponseSchemas)
def get_ai_model_by_id_router(
    model_id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> GetAiModelResponseSchemas:
    model = get_ai_model_by_id(model_id)
    if model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="模型不存在！")
    return GetAiModelResponseSchemas(
        id=str(model.id),
        name=model.name,
        api_key=model.api_key,
        base_url=model.base_url,
        is_active=model.is_active,
        model_type=model.model_type,
        test_status=model.test_status,
        provider_id=str(model.provider_id),
    )


@router.delete("/{model_id}", response_model=MessageResponseSchemas)
def delete_ai_model_router(
    model_id: UUID,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    model = get_ai_model_by_id(model_id)
    if model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="模型不存在！")
    delete_ai_model(model)
    return MessageResponseSchemas(detail="模型已删除！")
