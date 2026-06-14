from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from enums.ai_model import AiModelTestStatus

if TYPE_CHECKING:
    from database.ai_provider import AiProvider


class AiModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    test_status: AiModelTestStatus
    provider_id: UUID = Field(foreign_key="aiprovider.id", ondelete="CASCADE")
    provider: "AiProvider" = Relationship(back_populates="models")
