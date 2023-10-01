import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped

from core.base_classes.base_model import Base


class Subcategory(Base):
    __tablename__ = 'subcategories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(100))

    category_id: Mapped[int] = mapped_column(sa.ForeignKey('categories.id', ondelete='CASCADE'))
