from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from account.routers import router as account_router
from account.services import ensure_default_admin
from database import create_db_and_tables
from setting.routers import router as setting_router
from setting.services import ensure_default_setting


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    ensure_default_admin()
    ensure_default_setting()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(account_router)
app.include_router(setting_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}
