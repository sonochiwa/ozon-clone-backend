import sqlalchemy as sa
from slugify import slugify
from sqlalchemy.orm import mapped_column, Mapped

from core.base_classes.base_model import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(100), unique=True)
    # slug: Mapped[str] = mapped_column(sa.String(255), default=lambda: slugify(Category.name.default.arg), unique=True)
    slug: Mapped[str] = mapped_column(sa.String(255), unique=True)

    image_id: Mapped[int | None] = mapped_column(sa.ForeignKey('images.id', ondelete='CASCADE'))
