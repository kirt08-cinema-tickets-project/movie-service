from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import CategoriesORM

from src.categories.shemas import CategoryBaseDatabase


async def service_get_all_categories(session: AsyncSession) -> list[CategoryBaseDatabase]:
    data_orm = (await session.execute(select(CategoriesORM))).scalars().all()
    data_dto = [CategoryBaseDatabase.model_validate(data) for data in data_orm]
    return data_dto