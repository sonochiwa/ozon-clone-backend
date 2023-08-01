from sqlalchemy.ext.asyncio import AsyncSession

from core.base_classes.base_repository import BaseRepository
from core.db.models.product import Product


class ProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Product)
