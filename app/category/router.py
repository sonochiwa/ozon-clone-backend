from fastapi import APIRouter, Depends, Response
from starlette import status

from app.category.schema import CategoryReadSchema, CategoryCreateSchema, CategoryUpdateSchema
from app.category.service import CategoryService
from core.helpers.pagination_helper import Pagination

category_router = APIRouter()


@category_router.get(
    '/categories',
    tags=['Categories'],
    response_model=list[CategoryReadSchema],
    status_code=status.HTTP_200_OK,
)
async def read_all_categories(
        response: Response,
        pagination: Pagination = Depends(Pagination.get_pagination),
        service: CategoryService = Depends(),
):
    categories, total_count = await service.read_all_categories(pagination)
    response.headers["X-Total-Count"] = total_count
    return categories


@category_router.get(
    '/categories/{category_id}',
    tags=['Categories'],
    response_model=CategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def read_category(
        category_id: int,
        service: CategoryService = Depends()
):
    return await service.read_category(category_id)


@category_router.post(
    '/categories',
    tags=['Categories'],
    response_model=CategoryReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
        request: CategoryCreateSchema,
        service: CategoryService = Depends()
):
    return await service.create_category(request)


@category_router.put(
    '/categories/{category_id}',
    tags=['Categories'],
    response_model=CategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def update_category(
        request: CategoryUpdateSchema,
        category_id: int,
        service: CategoryService = Depends()
):
    return await service.update_category(request, category_id)


@category_router.delete(
    '/categories/{category_id}',
    tags=['Categories'],
    response_model=CategoryReadSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_category(
        category_id: int,
        service: CategoryService = Depends()
):
    return await service.delete_category(category_id)
