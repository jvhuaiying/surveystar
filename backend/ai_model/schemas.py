from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class GetAiModelResponseSchemas(BaseModel):
    id: str
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    provider_id: str
    created_at: datetime
    updated_at: datetime


class CreateAiModelRequestSchemas(BaseModel):
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    provider_id: UUID


class MessageResponseSchemas(BaseModel):
    detail: str
