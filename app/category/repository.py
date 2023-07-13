from sqlalchemy.ext.asyncio import AsyncSession

from app.category.model import Category
from core.base_classes.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Category)
