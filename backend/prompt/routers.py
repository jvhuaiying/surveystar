from typing import Annotated, Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from account.services import get_account_by_id
from auth import get_current_admin
from database import Account
from prompt.schemas import (
    CreateSystemPromptRequestSchemas,
    GetSystemPromptResponseSchemas,
    MessageResponseSchemas,
)
from prompt.services import (
    create_system_prompt,
    get_system_prompt_by_account_and_content,
    get_system_prompts,
)

router = APIRouter(prefix="/prompt", tags=["提示词管理"])


@router.post("/", response_model=MessageResponseSchemas)
def create_system_prompt_router(
    data: CreateSystemPromptRequestSchemas,
    admin: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    account = get_account_by_id(UUID(data.account_id))
    if account is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    existing = get_system_prompt_by_account_and_content(account, data.content)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="提示词内容已存在！")
    create_system_prompt(content=data.content, is_active=data.is_active, account=account)
    return MessageResponseSchemas(detail="提示词创建成功！")


@router.get("/", response_model=Sequence[GetSystemPromptResponseSchemas])
def get_system_prompts_router(
    admin: Annotated[Account, Depends(get_current_admin)],
) -> Sequence[GetSystemPromptResponseSchemas]:
    prompts = get_system_prompts()
    result = []
    for i in prompts:
        result.append(
            GetSystemPromptResponseSchemas(
                id=i["id"],
                content=i["content"],
                is_active=i["is_active"],
                account_id=i["account_id"],
                account_nickname=i["account_nickname"],
            )
        )
    return result
