import logging

from src.core.db import Database
from src.core.redis_db import (
    RedisService,
    MovieCacheKeys,
    MovieCacheService,
)

from src.movie.shemas import MovieDatabase, MovieDetailsDatabase
from src.movie.service import (
    service_list_movies,
    service_get_movie_by_slug,
    service_get_movie_by_id,
)

log = logging.getLogger(__name__)


class Movie:
    def __init__(self, db: Database, redis: RedisService):
        self._db = db
        self._redis = redis
        self._cache = MovieCacheService(redis = redis)
    
    async def list_movies(self, category: str, random: bool, limit: int) -> list[MovieDatabase]:
        cache_key = MovieCacheKeys.all(
            category = category,
            random = random,
            limit = limit
        )
        cache = await self._cache.getAll(cache_key)
        if cache:
            return cache
        

        async with self._db.session() as session:
            list_movies = await service_list_movies(
                category = category,
                random = random,
                limit = limit,
                session = session 
            )

        await self._cache.setAll(cache_key, list_movies)
        return list_movies
    

    async def get_movie_by_slug(self, slug: str) -> MovieDetailsDatabase:
        cache_key = MovieCacheKeys.bySlug(slug = slug)
        cache = await self._cache.getOne(key = cache_key)
        if cache:
            return cache

        async with self._db.session() as session:
            movie = await service_get_movie_by_slug(slug, session)

        await self._cache.setOne(key = cache_key, value = movie)
        return movie
    
    async def get_movie_by_id(self, id: str) -> MovieDetailsDatabase:
        cache_key = MovieCacheKeys.byId(id = id)
        cache = await self._cache.getOne(key = cache_key)
        if cache:
            return cache

        async with self._db.session() as session:
            movie = await service_get_movie_by_id(id, session)

        await self._cache.setOne(key = cache_key, value = movie)
        return movie