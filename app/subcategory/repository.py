from sqlalchemy.ext.asyncio import AsyncSession

from app.subcategory.model import Subcategory
from core.base_classes.base_repository import BaseRepository


class SubcategoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Subcategory)
