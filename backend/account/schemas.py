from pydantic import BaseModel, EmailStr

from enums.account import AccountKind


class SigninRequestSchemas(BaseModel):
    email: EmailStr
    password: str
    kind: AccountKind
    remember: bool = False


class SigninResponseSchemas(BaseModel):
    access_token: str
    id: str
    nickname: str
    email: EmailStr
    kind: AccountKind
    is_active: bool
