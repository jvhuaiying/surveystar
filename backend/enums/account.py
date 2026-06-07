from enum import StrEnum


class AccountKind(StrEnum):
    admin = "admin"
    user = "user"


class AccountStatus(StrEnum):
    active = "active"
    disabled = "disabled"
    deleted = "deleted"
