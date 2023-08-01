from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped

from core.base_classes.base_model import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(255))
    price: Mapped[float] = mapped_column(sa.Numeric(10, 2))
    count: Mapped[int] = mapped_column(sa.Integer, default=0)
    discount: Mapped[int] = mapped_column(sa.Integer, default=0)
    views: Mapped[int] = mapped_column(sa.Integer, default=0)
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    description: Mapped[str | None] = mapped_column(sa.String(1000))

    subcategory_id: Mapped[int] = mapped_column(sa.ForeignKey('subcategories.id'))
