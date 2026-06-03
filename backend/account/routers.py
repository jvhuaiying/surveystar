from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException, status

from account.schemas import SigninRequestSchemas, SigninResponseSchemas
from account.services import get_account, get_account_by_email, password_hash
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
    token = create_access_token({"sub": str(account.id)}, False)
    return SigninResponseSchemas(
        access_token=token,
        id=str(account.id),
        nickname=account.nickname,
        email=account.email,
        kind=account.kind,
        is_active=account.is_active,
    )


@router.get("/", response_model=Sequence[Account])
def get_account_router(
    account: Annotated[Account, Depends(get_current_admin)],
) -> Sequence[Account]:
    return get_account()
