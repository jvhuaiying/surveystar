from datetime import datetime, timedelta, timezone
from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from account.services import get_account_by_id
from database import Account
from enums.account import AccountKind
from settings import get_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, remember: bool) -> str:
    settings = get_settings()
    to_encode = data.copy()
    if remember:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60 * 24 * 7)
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60 * 24 * 30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, settings.algorithm)
    return encoded_jwt


async def get_current_account(token: Annotated[str, Depends(oauth2_scheme)]) -> Account:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        settings = get_settings()
        payload = jwt.decode(token, settings.secret_key, settings.algorithm)
        account_id = payload.get("sub")
        if account_id is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    try:
        account_uuid = UUID(account_id)
    except ValueError, TypeError:
        raise credentials_exception
    account = get_account_by_id(account_uuid)
    if account is None or not account.is_active:
        raise credentials_exception
    return account


async def get_current_admin(
    current_account: Annotated[Account, Depends(get_current_account)],
) -> Account:
    if current_account.kind != AccountKind.admin:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="权限错误！")
    return current_account
