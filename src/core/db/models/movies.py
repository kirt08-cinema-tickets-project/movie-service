import uuid
from datetime import datetime

from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.models.base_model import Base


if TYPE_CHECKING:
    from src.core.db.models import CategoriesORM

class MoviesORM(Base):
    __tablename__ = "movies"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    slug: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    poster: Mapped[str] = mapped_column(Text, nullable=False)
    banner: Mapped[str] = mapped_column(Text, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    release_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    release_year: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String(256))
    rating_age: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    category: Mapped[str] = mapped_column(ForeignKey("categories.slug"), nullable=True)
    categories_rel: Mapped["CategoriesORM"] = relationship(back_populates="movies_rel")
