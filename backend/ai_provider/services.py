from typing import Sequence
from uuid import UUID

from sqlmodel import Session, select

from database import engine
from database.ai_provider import AiProvider


def create_ai_provider(
    name: str,
    is_active: bool,
) -> AiProvider:
    provider = AiProvider(
        name=name,
        is_active=is_active,
    )
    with Session(engine) as session:
        session.add(provider)
        session.commit()
        session.refresh(provider)
    return provider


def get_ai_provider_by_name(name: str) -> AiProvider | None:
    with Session(engine) as session:
        statement = select(AiProvider).where(AiProvider.name == name)
        return session.exec(statement).first()


def get_ai_providers() -> Sequence[AiProvider]:
    with Session(engine) as session:
        statement = select(AiProvider)
        return session.exec(statement).all()


def get_ai_provider_by_id(id: UUID) -> AiProvider | None:
    with Session(engine) as session:
        statement = select(AiProvider).where(AiProvider.id == id)
        return session.exec(statement).first()


def update_ai_provider_status(provider: AiProvider, is_active: bool) -> AiProvider:
    provider.is_active = is_active
    with Session(engine) as session:
        session.add(provider)
        session.commit()
        session.refresh(provider)
    return provider


def update_ai_provider(
    provider: AiProvider,
    name: str,
    is_active: bool,
) -> AiProvider:
    provider.name = name
    provider.is_active = is_active
    with Session(engine) as session:
        session.add(provider)
        session.commit()
        session.refresh(provider)
    return provider


def delete_ai_provider(provider: AiProvider) -> None:
    with Session(engine) as session:
        session.delete(provider)
        session.commit()
