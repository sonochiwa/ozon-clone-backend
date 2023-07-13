from typing import TypeVar
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import func

from core.helpers.pagination_helper import Pagination
from core.utils.add_pagination import select_rows_with_pagination

TModel = TypeVar('TModel')
TCreateSchema = TypeVar('TCreateSchema')
TUpdateSchema = TypeVar('TUpdateSchema')


class BaseRepository:
    def __init__(
            self,
            session: AsyncSession,
            model: TModel,
    ) -> None:
        self.session = session
        self.model = model

    async def get_multi(self, pagination: Pagination) -> tuple[list[TModel], str]:
        query = await self.session.execute(
            select_rows_with_pagination(self.model, pagination)
        )

        total_count = await self.session.execute(
            select(func.count()).select_from(self.model)
        )

        return query.scalars().all(), str(total_count.one())

    async def get_by_id(self, row_id: int | UUID) -> TModel:
        query = await self.session.execute(
            select(self.model).where(self.model.id == row_id)
        )

        return query.scalar_one()

    async def create(self, request: TCreateSchema) -> TModel:
        stmt = self.model(**request.dict())
        self.session.add(stmt)
        await self.session.commit()

        return stmt

    async def update(self, request: TUpdateSchema, row_id: int | UUID) -> TModel:
        stmt = await self.get_by_id(row_id)

        for field, value in request:
            setattr(stmt, field, value)

        self.session.add(stmt)
        await self.session.commit()
        await self.session.refresh(stmt)

        return stmt

    async def delete(self, row_id: int | UUID) -> TModel:
        stmt = await self.session.execute(
            delete(self.model).where(self.model.id == row_id).returning(self.model)
        )

        return stmt.scalar_one()
