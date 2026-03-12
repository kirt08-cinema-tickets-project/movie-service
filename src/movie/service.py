from datetime import datetime

from sqlalchemy import select, Select, func
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

from src.core.db.models import MoviesORM

from src.movie.shemas import (
    MovieDatabase, 
    MovieDetailsDatabase,
)

from src.movie.exceptions import (
    InvalidDataException,
)


async def service_list_movies(category: str, random: bool, limit: int, session: AsyncSession) -> list[MovieDatabase]:
    query = _build_base_query()
    query = _build_query_where(query, category)
    query = _build_query_order(query, random)
    if limit and limit > 0:
        query = query.limit(limit)

    res_orm = (await session.execute(query)).scalars().all()
    res_dto = [MovieDatabase.model_validate(res) for res in res_orm]
    return res_dto

def _build_base_query() -> Select[tuple[MoviesORM]]:
    return select(MoviesORM).options(joinedload(MoviesORM.categories_rel))

def _build_query_where(query: Select[tuple[MoviesORM]], category: str) -> Select[tuple[MoviesORM]]:
    """
    Function that apply filter to quary
    """

    now = datetime.now()

    if category == "now":
        query.where(MoviesORM.release_date <= now)
    elif category == "soon":
        query.where((MoviesORM.release_date > now) | (MoviesORM.release_date.is_(None)))
    else:
        query.where(MoviesORM.category == category)
    return query

def _build_query_order(query: Select[tuple[MoviesORM]], random: bool) -> Select[tuple[MoviesORM]]:
    if random:
        return query.order_by(func.random())
    else:
        return query.order_by(MoviesORM.release_date.desc())


async def service_get_movie_by_slug(slug: str, session: AsyncSession) -> MovieDetailsDatabase:
    try:
        data_orm = (await session.execute(
            select(MoviesORM)
            .filter_by(slug = slug)
            .options(
                joinedload(MoviesORM.categories_rel)
            )
        )).scalars().one()
    except (NoResultFound, MultipleResultsFound):
        raise InvalidDataException
    
    data_dto = MovieDetailsDatabase.model_validate(data_orm)
    return data_dto

async def service_get_movie_by_id(id: str, session: AsyncSession) -> MovieDetailsDatabase:
    try:
        data_orm = (await session.execute(
            select(MoviesORM)
            .filter_by(id = id)
            .options(
                joinedload(MoviesORM.categories_rel)
            )
        )).one()
    except NoResultFound:
        raise InvalidDataException("Movie with such id doesn't exist")
    
    data_dto = MovieDetailsDatabase.model_validate(data_orm)
    return data_dto

