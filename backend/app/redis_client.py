import redis.asyncio as redis
from typing import Optional
from .config import settings
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return _redis

async def get_cached_balance(client_id: int) -> Optional[str]:
    r = await get_redis()
    return await r.get(f"balance:{client_id}")

async def set_cached_balance(client_id: int, value: str, expire_seconds: int = 3600):
    r = await get_redis()
    await r.set(f"balance:{client_id}", value, ex=expire_seconds)

