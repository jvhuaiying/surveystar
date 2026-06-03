from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from pwdlib import PasswordHash
from pydantic import EmailStr
from sqlmodel import Session, select

from database import engine
from database.account import Account
from enums.account import AccountKind

password_hash = PasswordHash.recommended()


def create_account(
    nickname: str,
    email: EmailStr,
    password: str,
    is_active: bool,
    kind: AccountKind,
    created_at: datetime,
    updated_at: datetime,
) -> Account:
    account = Account(
        nickname=nickname,
        email=email,
        password=password,
        is_active=is_active,
        kind=kind,
        created_at=created_at,
        updated_at=updated_at,
    )
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
    return account


def get_account() -> Sequence[Account]:
    with Session(engine) as session:
        statement = select(Account)
        return session.exec(statement).all()


def get_account_by_email(email: EmailStr) -> Account | None:
    with Session(engine) as session:
        statement = select(Account).where(Account.email == email)
        return session.exec(statement).first()


def get_account_by_id(id: UUID) -> Account | None:
    with Session(engine) as session:
        statement = select(Account).where(Account.id == id)
        return session.exec(statement).first()


def get_accounts_by_kind(kind: AccountKind) -> Sequence[Account]:
    with Session(engine) as session:
        statement = select(Account).where(Account.kind == kind)
        return session.exec(statement).all()


def ensure_default_admin() -> None:
    admin = get_accounts_by_kind(AccountKind.admin)
    if admin:
        return
    now = datetime.now(timezone.utc)
    hashed_password = password_hash.hash("admin123")
    create_account(
        nickname="admin",
        email="admin@admin.com",
        password=hashed_password,
        is_active=True,
        kind=AccountKind.admin,
        created_at=now,
        updated_at=now,
    )
