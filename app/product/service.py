from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.product.repository import ProductRepository
from app.product.schema import ProductCreateSchema
from app.subcategory.schema import SubcategoryCreateSchema, SubcategoryUpdateSchema
from core.base_classes.base_service import BaseService
from core.db.models.product import Product
from core.db.session import get_async_session
from core.enums.sort_enum import SortEnum
from core.exceptions.server_exception import ServerException
from core.helpers.filters_helper import Filter
from core.helpers.pagination_helper import Pagination


class ProductService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.product_repository = ProductRepository(session)

    async def read_all_products(
            self, pagination: Pagination,
            sort: SortEnum,
            filters: Filter
    ) -> tuple[list[Product], str]:
        return await self.product_repository.get_multi(pagination=pagination, sort=sort, filters=filters)

    async def read_product(self, subcategory_id: int) -> Product:
        try:
            subcategory = await self.product_repository.get_by_id(subcategory_id)
            return subcategory
        except Exception as e:
            raise ServerException(e)

    async def create_product(self, request: ProductCreateSchema) -> Product:
        try:
            subcategory = await self.product_repository.create(request)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def update_product(self, request: SubcategoryUpdateSchema, subcategory_id: int) -> Product:
        try:
            subcategory = await self.product_repository.update(request, subcategory_id)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def delete_product(self, subcategory_id: int) -> Product:
        try:
            subcategory = await self.product_repository.delete(subcategory_id)
            await self.session.commit()
            return subcategory
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)
