from sqlalchemy.ext.asyncio import AsyncSession

from core.base_classes.base_repository import BaseRepository
from core.database.models.subcategory import Subcategory


class SubcategoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Subcategory)
