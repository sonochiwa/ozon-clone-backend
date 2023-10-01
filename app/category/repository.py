from sqlalchemy.ext.asyncio import AsyncSession

from core.base_classes.base_repository import BaseRepository
from core.database.models.category import Category


class CategoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Category)

    async def create_category(self, request):
        self.session.add(request)

        return request
