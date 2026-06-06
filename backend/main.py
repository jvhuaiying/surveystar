from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from account.routers import router as account_router
from account.services import ensure_default_admin
from database import create_db_and_tables
from website_info.routers import router as website_info_router
from website_info.services import ensure_default_website_info


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    ensure_default_admin()
    ensure_default_website_info()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(account_router)
app.include_router(website_info_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}
