# backend/app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .database import engine, Base
from .redis_client import get_redis
from .api import api_router  # import from __init__.py

app = FastAPI(title="Collection System API")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await get_redis()


# Global exception middleware
@app.middleware("http")
async def global_exception_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Here you can add logging if needed
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)}
        )


# Include the combined router
app.include_router(api_router)
