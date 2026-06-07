import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from enums.account import AccountKind, AccountStatus


class Account(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nickname: str = Field(max_length=64)
    email: EmailStr = Field(unique=True)
    password: str = Field(max_length=128)
    status: AccountStatus
    kind: AccountKind
    created_at: datetime
    updated_at: datetime
