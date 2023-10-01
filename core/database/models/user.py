import sqlalchemy as sa
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column

from core.base_classes.base_model import Base
from core.database.mixins.timestamp_mixin import TimestampMixin


class User(Base, SQLAlchemyBaseUserTableUUID, TimestampMixin):
    __tablename__: str = 'users'

    first_name: Mapped[str] = mapped_column(sa.String(30))
    middle_name: Mapped[str] = mapped_column(sa.String(30))
    last_name: Mapped[str] = mapped_column(sa.String(30))
