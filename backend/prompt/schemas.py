from pydantic import BaseModel


class MessageResponseSchemas(BaseModel):
    detail: str


class CreateSystemPromptRequestSchemas(BaseModel):
    content: str
    is_active: bool
    account_id: str


class GetSystemPromptResponseSchemas(BaseModel):
    id: str
    content: str
    is_active: bool
    account_id: str
    account_nickname: str
