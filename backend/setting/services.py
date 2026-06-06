from sqlmodel import Session, select

from database import Setting, engine


def create_setting(logo: str, name: str, description: str, icp: str | None) -> Setting:
    setting = Setting(logo=logo, name=name, description=description, icp=icp)
    with Session(engine) as session:
        session.add(setting)
        session.commit()
        session.refresh(setting)
    return setting


def get_setting() -> Setting | None:
    with Session(engine) as session:
        statement = select(Setting)
        return session.exec(statement).first()


def update_setting_info(
    setting: Setting, name: str, description: str, icp: str | None
) -> Setting:
    setting.name = name
    setting.description = description
    setting.icp = icp
    with Session(engine) as session:
        session.add(setting)
        session.commit()
        session.refresh(setting)
    return setting


def update_setting_logo(setting: Setting, logo: str) -> Setting:
    setting.logo = logo
    with Session(engine) as session:
        session.add(setting)
        session.commit()
        session.refresh(setting)
    return setting


def ensure_default_setting():
    if get_setting() is None:
        create_setting(logo="logo.png", name="智研星", description="1", icp=None)
