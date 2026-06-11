from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.ai_model import AiModel


class AiProvider(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    is_active: bool
    models: list["AiModel"] = Relationship(back_populates="provider")
    created_at: datetime
    updated_at: datetime
