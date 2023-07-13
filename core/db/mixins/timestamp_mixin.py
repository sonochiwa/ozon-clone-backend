from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return mapped_column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
