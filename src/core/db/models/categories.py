import uuid

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.models.base_model import Base


if TYPE_CHECKING:
    from src.core.db.models import MoviesORM


class CategoriesORM(Base):
    __tablename__ = "categories"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    slug: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    movies_rel: Mapped[list["MoviesORM"]] = relationship(back_populates="categories_rel")