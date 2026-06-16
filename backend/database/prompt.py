from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.account import Account


class SystemPrompt(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    content: str
    is_active: bool
    account_id: UUID = Field(foreign_key="account.id", ondelete="CASCADE")
    account: "Account" = Relationship(back_populates="system_prompts")
