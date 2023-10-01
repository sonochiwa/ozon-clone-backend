import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped

from core.base_classes.base_model import Base


class Image(Base):
    __tablename__ = 'images'

    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[int] = mapped_column(sa.String(255))
