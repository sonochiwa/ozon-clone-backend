import uuid
from datetime import datetime

from fastapi_users import schemas
from pydantic import Field


class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str | None = Field(None, max_length=30)
    middle_name: str | None = Field(None, max_length=30)
    last_name: str | None = Field(None, max_length=30)
    created_at: datetime | None = Field(None)
    updated_at: datetime | None = Field(None)


class UserCreate(schemas.BaseUserCreate):
    first_name: str = Field(..., max_length=30)
    middle_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str | None = Field(None, max_length=30)
    middle_name: str | None = Field(None, max_length=30)
    last_name: str | None = Field(None, max_length=30)
