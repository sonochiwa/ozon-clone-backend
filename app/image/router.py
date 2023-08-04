from fastapi import APIRouter, Depends, Response
from starlette import status

from app.image.schema import ImageGetSchema, ImageCreateSchema, ImageUpdateSchema
from app.image.service import ImageService
from core.helpers.pagination_helper import Pagination
from core.helpers.sort_helper import Sort
from core.utils.add_sort import SortEnum

image_router = APIRouter()


@image_router.get(
    '/images',
    tags=['Images'],
    response_model=list[ImageGetSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all_images(
        response: Response,
        pagination: Pagination = Depends(Pagination.get_pagination),
        sort: SortEnum = Depends(Sort.get_sort),
        service: ImageService = Depends(),
):
    images, total_count = await service.get_all_images(pagination, sort)
    response.headers["X-Total-Count"] = total_count
    return images


@image_router.get(
    '/images/{image_id}',
    tags=['Images'],
    response_model=ImageGetSchema,
    status_code=status.HTTP_200_OK,
)
async def get_image(
        image_id: int,
        service: ImageService = Depends()
):
    return await service.get_image(image_id)


@image_router.post(
    '/images',
    tags=['Images'],
    response_model=ImageGetSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_image(
        request: ImageCreateSchema,
        service: ImageService = Depends()
):
    return await service.add_image(request)


@image_router.put(
    '/images/{image_id}',
    tags=['Images'],
    response_model=ImageGetSchema,
    status_code=status.HTTP_200_OK,
)
async def update_image(
        request: ImageUpdateSchema,
        image_id: int,
        service: ImageService = Depends()
):
    return await service.update_image(request, image_id)


@image_router.delete(
    '/images/{image_id}',
    tags=['Images'],
    response_model=ImageGetSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_image(
        image_id: int,
        service: ImageService = Depends()
):
    return await service.delete_image(image_id)
