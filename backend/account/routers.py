from datetime import datetime, timezone
from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException, status

from account.schemas import (
    CreateAccountRequestSchemas,
    GetAccountResponseSchemas,
    SigninRequestSchemas,
    SigninResponseSchemas,
)
from account.services import (
    create_account,
    get_account,
    get_account_by_email,
    password_hash,
)
from auth import create_access_token, get_current_admin
from database import Account

router = APIRouter(prefix="/account", tags=["账号管理"])


@router.post("/signin", response_model=SigninResponseSchemas)
def signin_router(data: SigninRequestSchemas):
    account = get_account_by_email(data.email)
    if (
        account is None
        or not account.is_active
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
        is_active=account.is_active,
    )


@router.post("/", response_model=GetAccountResponseSchemas)
def create_account_router(
    data: CreateAccountRequestSchemas,
    account: Annotated[Account, Depends(get_current_admin)],
) -> GetAccountResponseSchemas:
    existing = get_account_by_email(data.email)
    if existing is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="邮箱已注册！")
    now = datetime.now(timezone.utc)
    hashed_password = password_hash.hash(data.password)
    account0 = create_account(
        nickname=data.nickname,
        email=data.email,
        password=hashed_password,
        is_active=data.is_active,
        kind=data.kind,
        created_at=now,
        updated_at=now,
    )
    return GetAccountResponseSchemas(
        id=str(account0.id),
        nickname=account0.nickname,
        email=account0.email,
        is_active=account0.is_active,
        kind=account0.kind,
        created_at=account0.created_at,
        updated_at=account0.updated_at,
    )


@router.get("/", response_model=Sequence[GetAccountResponseSchemas])
def get_account_router(
    account: Annotated[Account, Depends(get_current_admin)],
) -> Sequence[GetAccountResponseSchemas]:
    accounts = get_account()
    return [
        GetAccountResponseSchemas(
            id=str(a.id),
            nickname=a.nickname,
            email=a.email,
            is_active=a.is_active,
            kind=a.kind,
            created_at=a.created_at,
            updated_at=a.updated_at,
        )
        for a in accounts
    ]
