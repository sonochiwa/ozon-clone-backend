import os

from fastapi import Depends, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.image.repository import ImageRepository
from app.image.schema import ImageCreateSchema
from core.base_classes.base_service import BaseService
from core.database.models.image import Image
from core.database.session import get_async_session
from core.exceptions.server_exception import ServerException


class ImageService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.image_repository = ImageRepository(session)

    async def get_image(self, image_id: int) -> Image:
        try:
            image = await self.image_repository.get_by_id(image_id)
            return image.path
        except Exception as e:
            raise ServerException(e)

    async def upload_image(self, file: UploadFile) -> UploadFile:
        file_extensions = ['.png', '.jpg', '.jpeg', '.webp']
        file_extension = os.path.splitext(file.filename)

        if file_extension[1] not in file_extensions:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Unavailable file format')

        if file.size > 2000000:  # 2 MB
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'The image size must be less than 2 MB')

        try:
            file_location = f"s3/images/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())

            request = ImageCreateSchema(path=file_location)
            image = await self.image_repository.create(request)
            await self.session.commit()

            file.id = image.id
            return file
        except Exception as e:
            await self.session.rollback()
            raise ServerException(e)
