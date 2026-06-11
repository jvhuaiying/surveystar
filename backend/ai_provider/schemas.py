from datetime import datetime

from pydantic import BaseModel


class GetAiProviderResponseSchemas(BaseModel):
    id: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class CreateAiProviderRequestSchemas(BaseModel):
    name: str
    is_active: bool


class UpdateAiProviderRequestSchemas(BaseModel):
    name: str
    is_active: bool


class MessageResponseSchemas(BaseModel):
    detail: str
