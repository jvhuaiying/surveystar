from enum import StrEnum


class AiModelTestStatus(StrEnum):
    untested = "untested"
    success = "success"
    failed = "failed"
