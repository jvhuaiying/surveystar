import uuid
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class AiProvider(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    is_active: bool
    models: list["AiModel"] = Relationship(back_populates="provider")
    created_at: datetime
    updated_at: datetime


class AiModel(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    provider_id: uuid.UUID = Field(foreign_key="aiprovider.id")
    provider: AiProvider = Relationship(back_populates="models")
    created_at: datetime
    updated_at: datetime
