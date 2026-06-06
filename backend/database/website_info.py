import uuid

from sqlmodel import Field, SQLModel


class WebsiteInfo(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    logo: str
    name: str = Field(max_length=36)
    description: str = Field(max_length=64)
    icp: str | None = Field(default=None, max_length=128)
