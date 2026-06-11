from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from pwdlib import PasswordHash
from pydantic import EmailStr
from sqlmodel import Session, select

from database import engine
from database.account import Account
from enums.account import AccountKind, AccountStatus

password_hash = PasswordHash.recommended()


def create_account(
    nickname: str,
    email: EmailStr,
    password: str,
    status: AccountStatus,
    kind: AccountKind,
) -> Account:
    now = datetime.now(timezone.utc)
    account = Account(
        nickname=nickname,
        email=email,
        password=password,
        status=status,
        kind=kind,
        created_at=now,
        updated_at=now,
    )
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
    return account


def get_account() -> Sequence[Account]:
    with Session(engine) as session:
        statement = select(Account).where(Account.status != AccountStatus.deleted)
        return session.exec(statement).all()


def get_account_by_email(email: EmailStr) -> Account | None:
    with Session(engine) as session:
        statement = select(Account).where(
            Account.email == email, Account.status != AccountStatus.deleted
        )
        return session.exec(statement).first()


def get_account_by_id(id: UUID) -> Account | None:
    with Session(engine) as session:
        statement = select(Account).where(
            Account.id == id, Account.status != AccountStatus.deleted
        )
        return session.exec(statement).first()


def get_accounts_by_kind(kind: AccountKind) -> Sequence[Account]:
    with Session(engine) as session:
        statement = select(Account).where(
            Account.kind == kind, Account.status != AccountStatus.deleted
        )
        return session.exec(statement).all()


def get_active_admin_size() -> int:
    with Session(engine) as session:
        statement = select(Account).where(
            Account.kind == AccountKind.admin, Account.status == AccountStatus.active
        )
        return len(session.exec(statement).all())


def update_account_status(account: Account, status: AccountStatus):
    account.status = status
    with Session(engine) as session:
        session.add(account)
        session.commit()


def update_account(
    account: Account,
    nickname: str,
    email: EmailStr,
    status: AccountStatus,
    kind: AccountKind,
) -> Account:
    account.nickname = nickname
    account.email = email
    account.status = status
    account.kind = kind
    account.updated_at = datetime.now(timezone.utc)
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
    return account


def ensure_default_admin() -> None:
    admin = get_accounts_by_kind(AccountKind.admin)
    if admin:
        return
    hashed_password = password_hash.hash("admin123")
    create_account(
        nickname="admin",
        email="admin@admin.com",
        password=hashed_password,
        status=AccountStatus.active,
        kind=AccountKind.admin,
    )
