from fastapi import APIRouter, Depends, Response
from starlette import status

from app.subcategory.schema import SubcategoryReadSchema, SubcategoryCreateSchema, SubcategoryUpdateSchema
from app.subcategory.service import SubcategoryService
from core.helpers.pagination_helper import Pagination

subcategory_router = APIRouter()


@subcategory_router.get(
    '/subcategories',
    tags=['Subcategories'],
    response_model=list[SubcategoryReadSchema],
    status_code=status.HTTP_200_OK,
)
async def read_all_subcategories(
        response: Response,
        pagination: Pagination = Depends(Pagination.get_pagination),
        service: SubcategoryService = Depends(),
):
    subcategories, total_count = await service.read_all_subcategories(pagination)
    response.headers["X-Total-Count"] = total_count
    return subcategories


@subcategory_router.get(
    '/subcategories/{subcategory_id}',
    tags=['Subcategories'],
    response_model=SubcategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def read_subcategory(
        subcategory_id: int,
        service: SubcategoryService = Depends()
):
    return await service.read_subcategory(subcategory_id)


@subcategory_router.post(
    '/subcategories',
    tags=['Subcategories'],
    response_model=SubcategoryReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_subcategory(
        request: SubcategoryCreateSchema,
        service: SubcategoryService = Depends()
):
    return await service.create_subcategory(request)


@subcategory_router.put(
    '/subcategories/{subcategory_id}',
    tags=['Subcategories'],
    response_model=SubcategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def update_subcategory(
        request: SubcategoryUpdateSchema,
        subcategory_id: int,
        service: SubcategoryService = Depends()
):
    return await service.update_subcategory(request, subcategory_id)


@subcategory_router.delete(
    '/subcategories/{subcategory_id}',
    tags=['Subcategories'],
    response_model=SubcategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_subcategory(
        subcategory_id: int,
        service: SubcategoryService = Depends()
):
    return await service.delete_subcategory(subcategory_id)
