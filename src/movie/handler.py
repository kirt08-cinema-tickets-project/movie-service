import logging

from src.core.db import Database

from src.movie.shemas import MovieDatabase
from src.movie.service import (
    service_list_movies,
    service_get_movie_by_slug,
    service_get_movie_by_id,
)

log = logging.getLogger(__name__)


class Movie:
    def __init__(self, db: Database):
        self._db = db
    
    async def list_movies(self, category: str, random: bool, limit: int) -> list[MovieDatabase]:
        async with self._db.session() as session:
            list_movies = await service_list_movies(
                category = category,
                random = random,
                limit = limit,
                session = session 
            )
        return list_movies
    
    async def get_movie_by_slug(self, slug: str) -> MovieDatabase:
        async with self._db.session() as session:
            movie = await service_get_movie_by_slug(slug, session)
        return movie
    
    async def get_movie_by_id(self, id: str) -> MovieDatabase:
        async with self._db.session() as session:
            movie = await service_get_movie_by_id(id, session)
        return movie