from typing import TypeVar
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import func

from core.helpers.filters_helper import Filter
from core.helpers.pagination_helper import Pagination
from core.utils.add_filters import add_filters
from core.utils.add_pagination import add_pagination
from core.utils.add_sort import add_sort, SortEnum

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

    async def get_multi(
            self,
            pagination: Pagination = None,
            sort: SortEnum = None,
            filters: Filter = None,
    ):
        query = select(self.model)

        if pagination:
            query = add_pagination(query, pagination)

        if filters:
            query = add_filters(query, filters, self.model)

        if sort:
            query = add_sort(query, sort, self.model)

        result = await self.session.execute(query)

        total_count = await self.session.execute(
            select(func.count()).select_from(self.model)
        )

        return result.scalars().all(), str(total_count.scalar_one())

    async def get_by_id(self, row_id: int | UUID):
        query = await self.session.execute(
            select(self.model).where(self.model.id == row_id)
        )

        return query.scalar_one()

    async def create(self, request: TCreateSchema):
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

    async def delete(self, row_id: int | UUID):
        stmt = await self.session.execute(
            delete(self.model).where(self.model.id == row_id).returning(self.model)
        )

        return stmt.scalar_one()
