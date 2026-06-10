from sqlmodel import SQLModel, create_engine

from database.account import Account
from database.ai_model import AiModel, AiProvider
from database.website_info import WebsiteInfo

engine = create_engine(
    "sqlite:///database.db", connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


__all__ = [
    "create_db_and_tables",
    "engine",
    "Account",
    "AiModel",
    "AiProvider",
    "WebsiteInfo",
]
