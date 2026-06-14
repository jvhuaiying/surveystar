from uuid import UUID

from pydantic import BaseModel

from enums.ai_model import AiModelTestStatus


class GetAiModelResponseSchemas(BaseModel):
    id: str
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    test_status: AiModelTestStatus
    provider_id: str


class CreateAiModelRequestSchemas(BaseModel):
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    provider_id: UUID


class UpdateAiModelRequestSchemas(BaseModel):
    name: str
    api_key: str
    base_url: str
    is_active: bool
    model_type: str
    provider_id: UUID


class MessageResponseSchemas(BaseModel):
    detail: str
