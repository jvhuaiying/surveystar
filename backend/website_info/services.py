from sqlmodel import Session, select

from database import WebsiteInfo, engine


def create_website_info(
    logo: str, name: str, description: str, icp: str | None
) -> WebsiteInfo:
    website_info = WebsiteInfo(logo=logo, name=name, description=description, icp=icp)
    with Session(engine) as session:
        session.add(website_info)
        session.commit()
        session.refresh(website_info)
    return website_info


def get_website_info() -> WebsiteInfo | None:
    with Session(engine) as session:
        statement = select(WebsiteInfo)
        return session.exec(statement).first()


def update_website_info(
    website_info: WebsiteInfo, name: str, description: str, icp: str | None
) -> WebsiteInfo:
    website_info.name = name
    website_info.description = description
    website_info.icp = icp
    with Session(engine) as session:
        session.add(website_info)
        session.commit()
        session.refresh(website_info)
    return website_info


def update_website_info_logo(website_info: WebsiteInfo, logo: str) -> WebsiteInfo:
    website_info.logo = logo
    with Session(engine) as session:
        session.add(website_info)
        session.commit()
        session.refresh(website_info)
    return website_info


def ensure_default_website_info():
    if get_website_info() is None:
        create_website_info(logo="logo.png", name="智研星", description="1", icp=None)
