from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException, UploadFile, status

from database.website_info import WebsiteInfo
from settings import get_settings
from website_info.schemas import UpdateWebsiteInfoRequestSchema
from website_info.services import (
    get_website_info,
    update_website_info,
    update_website_info_logo,
)

router = APIRouter(prefix="/website-info", tags=["网站信息"])


@router.get("/", response_model=WebsiteInfo)
def get_website_info_router() -> WebsiteInfo:
    website_info = get_website_info()
    if website_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="系统设置不存在！"
        )
    website_info.logo = "static/logo/" + website_info.logo
    return website_info


@router.put("/", response_model=WebsiteInfo)
def update_website_info_router(data: UpdateWebsiteInfoRequestSchema):
    info0 = get_website_info()
    if info0 is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "系统设置不存在！")
    info1 = update_website_info(info0, data.name, data.description, data.icp)
    info1.logo = "static/logo/" + info1.logo
    return info1


@router.post("/logo")
async def update_website_info_logo_router(logo: UploadFile):
    settings = get_settings()
    filename = logo.filename
    info0 = get_website_info()
    if info0 is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "系统设置不存在！")
    if filename is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "文件名不能为空！")
    file_ext = Path(filename).suffix
    file_path = str(uuid4()) + file_ext
    with open((settings.logo_folder / file_path), "wb") as f:
        f.write(await logo.read())
    info1 = update_website_info_logo(info0, file_path)
    info1.logo = "static/logo/" + info1.logo
    return info1
