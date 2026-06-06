from pydantic import BaseModel


class UpdateWebsiteInfoRequestSchema(BaseModel):
    name: str
    description: str
    icp: str | None
