from fastapi import APIRouter, Depends, UploadFile
from starlette import status
from starlette.responses import FileResponse

from app.image.schema import ImageGetSchema
from app.image.service import ImageService

image_router = APIRouter()


@image_router.get(
    '/images/{image_id}',
    tags=['Images'],
    status_code=status.HTTP_200_OK,
)
async def get_image(
        image_id: int,
        service: ImageService = Depends()
):
    result = await service.get_image(image_id)
    return FileResponse(result)


@image_router.post(
    '/images',
    tags=['Images'],
    response_model=ImageGetSchema,
    status_code=status.HTTP_201_CREATED,
)
async def upload_image(
        file: UploadFile,
        service: ImageService = Depends()
):
    return await service.upload_image(file)
