from src.core.db import Database

from src.categories.shemas import CategoryBaseDatabase

from src.categories.service import (
    service_get_all_categories,
)

class Category:
    def __init__(self, db: Database):
        self._db: Database = db

    async def get_all_categories(self) -> list[CategoryBaseDatabase]:
        async with self._db.session() as session: 
            res = await service_get_all_categories(session = session)
        return res