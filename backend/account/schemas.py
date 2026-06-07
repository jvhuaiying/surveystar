from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from enums.account import AccountKind, AccountStatus


class SigninRequestSchemas(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    kind: AccountKind
    remember: bool = False


class SigninResponseSchemas(BaseModel):
    access_token: str
    id: str
    nickname: str
    email: EmailStr
    kind: AccountKind
    status: AccountStatus


class CreateAccountRequestSchemas(BaseModel):
    nickname: str = Field(max_length=64)
    email: EmailStr
    password: str = Field(min_length=8)
    status: AccountStatus
    kind: AccountKind


class MessageResponseSchemas(BaseModel):
    detail: str


class GetAccountResponseSchemas(BaseModel):
    id: str
    nickname: str
    email: EmailStr
    status: AccountStatus
    kind: AccountKind
    created_at: datetime
    updated_at: datetime
