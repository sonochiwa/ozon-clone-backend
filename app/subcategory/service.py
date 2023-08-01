from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.subcategory.model import Subcategory
from app.subcategory.repository import SubcategoryRepository
from app.subcategory.schema import SubcategoryCreateSchema, SubcategoryUpdateSchema
from core.base_classes.base_service import BaseService
from core.db.session import get_async_session
from core.exceptions.server_exception import ServerException


class SubcategoryService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.subcategory_repository = SubcategoryRepository(session)

    async def read_all_subcategories(self, pagination, sort, filters) -> tuple[list[Subcategory], str]:
        return await self.subcategory_repository.get_multi(pagination=pagination, sort=sort, filters=filters)

    async def read_subcategory(self, subcategory_id: int) -> Subcategory:
        try:
            subcategory = await self.subcategory_repository.get_by_id(subcategory_id)
            return subcategory
        except Exception as e:
            raise ServerException(e)

    async def create_subcategory(self, request: SubcategoryCreateSchema) -> Subcategory:
        try:
            subcategory = await self.subcategory_repository.create(request)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def update_subcategory(self, request: SubcategoryUpdateSchema, subcategory_id: int) -> Subcategory:
        try:
            subcategory = await self.subcategory_repository.update(request, subcategory_id)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def delete_subcategory(self, subcategory_id: int) -> Subcategory:
        try:
            subcategory = await self.subcategory_repository.delete(subcategory_id)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)
