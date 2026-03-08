import logging

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.seed import CATEGORIES, MOVIES

from src.core.db.models.categories import CategoriesORM
from src.core.db.models.movies import MoviesORM


log = logging.getLogger(__name__)


async def service_insert_all_data_from_seed(session: AsyncSession) -> None:
    """
    Function to insert all data to database from seed.py
    """

    log.info("start to insert data from seed.py")
    await _service_insert_categories(session = session)
    await _service_insert_movies(session = session)
    await session.commit()
    log.info("movies and categories created")
    


async def _service_insert_categories(session: AsyncSession) -> None:
    query = insert(CategoriesORM).values(CATEGORIES)
    query = query.on_conflict_do_nothing(index_elements=["slug"])
    await session.execute(query)
    # await session.commit()

async def _service_insert_movies(session: AsyncSession) -> None:
    query = insert(MoviesORM).values(MOVIES)
    query = query.on_conflict_do_nothing(index_elements=["slug"])
    await session.execute(query)
    # await session.commit()