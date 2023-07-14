from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.category.model import Category
from app.category.repository import CategoryRepository
from app.category.schema import CategoryCreateSchema, CategoryUpdateSchema
from core.base_classes.base_service import BaseService
from core.db.session import get_async_session
from core.exceptions.server_exception import ServerException
from core.helpers.pagination_helper import Pagination


class CategoryService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.category_repository = CategoryRepository(session)

    async def read_all_categories(self, pagination: Pagination) -> tuple[list[Category], str]:
        return await self.category_repository.get_multi(pagination)

    async def read_category(self, category_id: int) -> Category:
        try:
            category = await self.category_repository.get_by_id(category_id)
            return category
        except Exception as e:
            raise ServerException(e)

    async def create_category(self, request: CategoryCreateSchema) -> Category:
        try:
            category = await self.category_repository.create(request)
            return category
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def update_category(self, request: CategoryUpdateSchema, category_id: int) -> Category:
        try:
            category = await self.category_repository.update(request, category_id)
            return category
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def delete_category(self, category_id: int) -> Category:
        try:
            category = await self.category_repository.delete(category_id)
            await self.session.commit()
            return category
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)
