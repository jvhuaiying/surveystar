from pydantic import BaseModel


class UpdateSettingRequestSchema(BaseModel):
    name: str
    description: str
    icp: str | None
