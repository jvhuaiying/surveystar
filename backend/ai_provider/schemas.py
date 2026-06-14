from pydantic import BaseModel


class GetAiProviderResponseSchemas(BaseModel):
    id: str
    name: str
    is_active: bool


class CreateAiProviderRequestSchemas(BaseModel):
    name: str
    is_active: bool


class UpdateAiProviderRequestSchemas(BaseModel):
    name: str
    is_active: bool


class MessageResponseSchemas(BaseModel):
    detail: str
