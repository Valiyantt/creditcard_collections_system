# backend/app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .redis_client import get_redis
from .api import api_router  # import from __init__.py

app = FastAPI(title="Collection System API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await get_redis()

# Include the combined router
app.include_router(api_router)
