from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Movie(BaseModel):
    id: UUID
    title: str
    slug: str
    poster: str
    rating_age: int
    release_date: datetime | None
    category: str | None

class Category(BaseModel):
    model_config =ConfigDict(
        from_attributes=True
    )

    id: UUID
    title: str
    slug: str

class MovieDatabase(Movie):
    model_config = ConfigDict(
        from_attributes=True
    )
    categories_rel: Category | None