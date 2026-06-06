from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException, UploadFile, status

from config import get_config
from database.settings import Setting
from setting.schemas import UpdateSettingRequestSchema
from setting.services import get_setting, update_setting_info, update_setting_logo

router = APIRouter(prefix="/settings", tags=["系统设置"])


@router.get("/", response_model=Setting)
def get_setting_router() -> Setting:
    setting = get_setting()
    if setting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="系统设置不存在！"
        )
    setting.logo = "static/logo/" + setting.logo
    return setting


@router.put("/", response_model=Setting)
def update_setting_info_router(setting: UpdateSettingRequestSchema):
    setting0 = get_setting()
    if setting0 is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "系统设置不存在！")
    setting1 = update_setting_info(
        setting0, setting.name, setting.description, setting.icp
    )
    setting1.logo = "static/logo/" + setting1.logo
    return setting1


@router.post("/logo")
async def update_setting_logo_router(logo: UploadFile):
    config = get_config()
    filename = logo.filename
    setting0 = get_setting()
    if setting0 is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "系统设置不存在！")
    if filename is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "文件名不能为空！")
    file_ext = Path(filename).suffix
    file_path = str(uuid4()) + file_ext
    with open((config.logo_folder / file_path), "wb") as f:
        f.write(await logo.read())
    setting1 = update_setting_logo(setting0, file_path)
    setting1.logo = "static/logo/" + setting1.logo
    return setting1
