from datetime import datetime, timezone
from typing import Annotated, Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from account.schemas import (
    CreateAccountRequestSchemas,
    GetAccountResponseSchemas,
    MessageResponseSchemas,
    SigninRequestSchemas,
    SigninResponseSchemas,
    UpdateAccountRequestSchemas,
)
from account.services import (
    create_account,
    delete_account,
    get_account,
    get_account_by_email,
    get_account_by_id,
    get_active_admin_size,
    password_hash,
    update_account,
    update_account_status,
)
from auth import create_access_token, get_current_admin
from database import Account
from enums.account import AccountKind, AccountStatus

router = APIRouter(prefix="/account", tags=["账号管理"])


@router.post("/signin", response_model=SigninResponseSchemas)
def signin_router(data: SigninRequestSchemas):
    account = get_account_by_email(data.email)
    if (
        account is None
        or account.status != AccountStatus.active
        or account.kind != data.kind
        or not password_hash.verify(data.password, account.password)
    ):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="邮箱或密码错误！")
    token = create_access_token({"sub": str(account.id)}, data.remember)
    return SigninResponseSchemas(
        access_token=token,
        id=str(account.id),
        nickname=account.nickname,
        email=account.email,
        kind=account.kind,
        status=account.status,
    )


@router.post("/", response_model=MessageResponseSchemas)
def create_account_router(
    data: CreateAccountRequestSchemas,
    account: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    existing = get_account_by_email(data.email)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="邮箱已注册！")
    hashed_password = password_hash.hash(data.password)
    create_account(
        nickname=data.nickname,
        email=data.email,
        password=hashed_password,
        status=data.status,
        kind=data.kind,
    )
    return MessageResponseSchemas(detail="账号创建成功！")


@router.get("/", response_model=Sequence[GetAccountResponseSchemas])
def get_account_router(
    account: Annotated[Account, Depends(get_current_admin)],
) -> Sequence[GetAccountResponseSchemas]:
    accounts = get_account()
    return [
        GetAccountResponseSchemas(
            id=str(account0.id),
            nickname=account0.nickname,
            email=account0.email,
            status=account0.status,
            kind=account0.kind,
            created_at=account0.created_at,
            updated_at=account0.updated_at,
        )
        for account0 in accounts
    ]


@router.get("/{id}", response_model=GetAccountResponseSchemas)
def get_account_by_id_router(
    id: UUID,
    account: Annotated[Account, Depends(get_current_admin)],
) -> GetAccountResponseSchemas:
    target = get_account_by_id(id)
    if target is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    return GetAccountResponseSchemas(
        id=str(target.id),
        nickname=target.nickname,
        email=target.email,
        status=target.status,
        kind=target.kind,
        created_at=target.created_at,
        updated_at=target.updated_at,
    )


@router.patch("/{id}", response_model=MessageResponseSchemas)
def update_account_router(
    id: UUID,
    data: UpdateAccountRequestSchemas,
    account: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    target = get_account_by_id(id)
    if target is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    if target.email != data.email:
        existing = get_account_by_email(data.email)
        if existing is not None:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="邮箱已被注册！")
    if target.kind == AccountKind.admin and data.kind != AccountKind.admin:
        if get_active_admin_size() < 2:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail="处于激活状态的管理员账号不足！"
            )
    update_account(
        target,
        nickname=data.nickname,
        email=data.email,
        status=data.status,
        kind=data.kind,
    )
    return MessageResponseSchemas(detail="账号修改成功！")


@router.patch("/{id}/disable", response_model=MessageResponseSchemas)
def disable_account_router(
    id: UUID,
    account: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    target = get_account_by_id(id)
    if target is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    if target.kind == AccountKind.admin and get_active_admin_size() < 2:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="处于激活状态的管理员账号不足！"
        )
    update_account_status(target, AccountStatus.disabled)
    return MessageResponseSchemas(detail="账号已禁用！")


@router.delete("/{id}", response_model=MessageResponseSchemas)
def delete_account_router(
    id: UUID,
    account: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    target = get_account_by_id(id)
    if target is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    if target.kind == AccountKind.admin and get_active_admin_size() < 2:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="处于激活状态的管理员账号不足！"
        )
    delete_account(target)
    return MessageResponseSchemas(detail="账号删除成功！")


@router.patch("/{id}/activate", response_model=MessageResponseSchemas)
def activate_account_router(
    id: UUID,
    account: Annotated[Account, Depends(get_current_admin)],
) -> MessageResponseSchemas:
    target = get_account_by_id(id)
    if target is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="账号不存在！")
    update_account_status(target, AccountStatus.active)
    return MessageResponseSchemas(detail="账号激活成功！")
