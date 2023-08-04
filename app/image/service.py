from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.image.repository import ImageRepository
from app.image.schema import ImageCreateSchema, ImageUpdateSchema
from core.base_classes.base_service import BaseService
from core.db.models.image import Image
from core.db.session import get_async_session
from core.exceptions.server_exception import ServerException


class ImageService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.image_repository = ImageRepository(session)

    async def get_all_images(self, pagination, sort) -> tuple[list[Image], str]:
        return await self.image_repository.get_multi(pagination=pagination, sort=sort)

    async def get_image(self, image_id: int) -> Image:
        try:
            image = await self.image_repository.get_by_id(image_id)
            return image
        except Exception as e:
            raise ServerException(e)

    async def add_image(self, request: ImageCreateSchema) -> Image:
        try:
            image = await self.image_repository.create(request)
            await self.session.commit()
            return image
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def update_image(self, request: ImageUpdateSchema, image_id: int) -> Image:
        try:
            image = await self.image_repository.update(request, image_id)
            await self.session.commit()
            return image
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)

    async def delete_image(self, image_id: int) -> Image:
        try:
            image = await self.image_repository.delete(image_id)
            await self.session.commit()
            return image
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)
