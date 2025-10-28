import os
import aioredis
from typing import Optional

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    return _redis

async def get_cached_balance(client_id: int) -> Optional[str]:
    r = await get_redis()
    return await r.get(f"balance:{client_id}")

async def set_cached_balance(client_id: int, value: str, expire_seconds: int = 3600):
    r = await get_redis()
    await r.set(f"balance:{client_id}", value, ex=expire_seconds)
