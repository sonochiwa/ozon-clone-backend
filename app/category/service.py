from fastapi import Depends
from slugify import slugify
from sqlalchemy.ext.asyncio import AsyncSession

from app.category.repository import CategoryRepository
from app.category.schema import CategoryCreateSchema, CategoryUpdateSchema
from core.base_classes.base_service import BaseService
from core.database.models.category import Category
from core.database.session import get_async_session
from core.exceptions.server_exception import ServerException


class CategoryService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.category_repository = CategoryRepository(session)

    async def get_all_categories(self, pagination, sort) -> tuple[list[Category], str]:
        return await self.category_repository.get_multi(pagination=pagination, sort=sort)

    async def create_category(self, request: CategoryCreateSchema) -> Category:
        try:
            stmt = Category(**request.dict())

            stmt.name = request.name
            stmt.slug = str(slugify(request.name))
            stmt.image_id = request.image_id

            category = await self.category_repository.create_category(stmt)
            await self.session.commit()
            return category
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def update_category(self, request: CategoryUpdateSchema, category_id: int) -> Category:
        try:
            category = await self.category_repository.update(request, category_id)
            await self.session.commit()
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
