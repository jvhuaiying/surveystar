from sqlmodel import SQLModel, create_engine

engine = create_engine(
    "sqlite:///database.db", connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


__all__ = ["create_db_and_tables", "engine"]
