from functools import lru_cache
import redis.asyncio as redis

from src.core.config import settings


@lru_cache
def get_redis_client() -> redis.Redis:
    print(settings.redis.url)
    pool = redis.ConnectionPool.from_url(
        settings.redis.url,
        max_connections=20,
        socket_timeout=2,
        socket_connect_timeout=2,
        retry_on_timeout=True,
    )

    return redis.Redis(
        connection_pool = pool,
        retry_on_timeout=True
    )


class RedisService:
    def __init__(self, client: redis.Redis):
        self._client = client

    async def get(self, key: str) -> str | None:
        return await self._client.get(key)
    
    async def set(self, key: str, value, ex : int | None = None):
        return await self._client.set(key, value, ex = ex)
    
    async def delete(self, key: str) -> bool:
        return bool(await self._client.delete(key))
    

async def get_redis() -> RedisService:
    client = get_redis_client()
    return RedisService(client = client)