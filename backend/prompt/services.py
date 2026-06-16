from sqlmodel import Session, select

from database import engine
from database.account import Account
from database.prompt import SystemPrompt


def create_system_prompt(
    content: str, is_active: bool, account: Account
) -> SystemPrompt:
    prompt = SystemPrompt(content=content, is_active=is_active, account_id=account.id)
    with Session(engine) as session:
        session.add(prompt)
        session.commit()
        session.refresh(prompt)
    return prompt


def get_system_prompts() -> list[dict]:
    with Session(engine) as session:
        statement = select(SystemPrompt)
        prompts = session.exec(statement).all()
        result = []
        for i in prompts:
            result.append(
                {
                    "id": str(i.id),
                    "content": i.content,
                    "is_active": i.is_active,
                    "account_id": str(i.account_id),
                    "account_nickname": i.account.nickname,
                }
            )
        return result


def get_system_prompt_by_account_and_content(
    account: Account, content: str
) -> SystemPrompt | None:
    with Session(engine) as session:
        statement = select(SystemPrompt).where(
            SystemPrompt.account_id == account.id,
            SystemPrompt.content == content,
        )
        return session.exec(statement).first()
