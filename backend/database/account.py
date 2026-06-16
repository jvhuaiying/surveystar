from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from enums.account import AccountKind, AccountStatus

if TYPE_CHECKING:
    from database.prompt import SystemPrompt


class Account(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nickname: str = Field(max_length=64)
    email: EmailStr
    password: str = Field(max_length=128)
    status: AccountStatus
    kind: AccountKind
    system_prompts: list["SystemPrompt"] = Relationship(
        back_populates="account", cascade_delete=True
    )
