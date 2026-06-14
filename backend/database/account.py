from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from enums.account import AccountKind, AccountStatus


class Account(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nickname: str = Field(max_length=64)
    email: EmailStr
    password: str = Field(max_length=128)
    status: AccountStatus
    kind: AccountKind
