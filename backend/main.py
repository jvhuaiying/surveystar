from contextlib import asynccontextmanager

from fastapi import FastAPI

from account.routers import router as account_router
from account.services import ensure_default_admin
from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    ensure_default_admin()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(account_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
