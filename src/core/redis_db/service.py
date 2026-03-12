from pydantic import TypeAdapter

from src.movie.shemas import MovieDatabase, MovieDetailsDatabase

from src.core.redis_db.redis import RedisService
from src.core.config import settings

class MovieCacheService:
    def __init__(self, redis: RedisService):
        self._redis = redis
        self._adapter = TypeAdapter(list[MovieDatabase])

    async def getOne(self, key: str) -> MovieDetailsDatabase | None:
        cached = await self._redis.get(key = key)
        if cached is None:
            return None
        cached_str = cached.decode()
        return MovieDetailsDatabase.model_validate_json(cached_str)

    async def setOne(self, key: str, value: MovieDetailsDatabase):
        cached_value = value.model_dump_json()
        await self._redis.set(key = key, value = cached_value, ex = settings.cache.ttl)

    async def getAll(self, key: str) -> list[MovieDatabase] | None:
        cached = await self._redis.get(key=key)

        if cached is None:
            return None

        return self._adapter.validate_json(cached)

    async def setAll(self, key: str, value: list[MovieDatabase]) -> None:
        value_cache = self._adapter.dump_json(value)

        await self._redis.set(key=key, value=value_cache, ex = settings.cache.ttl)
