from fastapi import APIRouter, Depends, Response
from starlette import status

from app.subcategory.helpers import SubcategoryHelper
from app.subcategory.schema import SubcategoryGetSchema, SubcategoryCreateSchema, SubcategoryUpdateSchema
from app.subcategory.service import SubcategoryService
from core.enums.sort_enum import SortEnum
from core.helpers.filters_helper import Filter
from core.helpers.pagination_helper import Pagination
from core.helpers.sort_helper import Sort

subcategory_router = APIRouter()


@subcategory_router.get(
    '/subcategories',
    tags=['Subcategories'],
    response_model=list[SubcategoryGetSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all_subcategories(
        response: Response,
        pagination: Pagination = Depends(Pagination.get_pagination),
        sort: SortEnum = Depends(Sort.get_sort),
        filters: Filter = Depends(SubcategoryHelper.get_filter),
        service: SubcategoryService = Depends(),
):
    subcategories, total_count = await service.get_all_subcategories(pagination, sort, filters)
    response.headers["X-Total-Count"] = total_count
    return subcategories


@subcategory_router.get(
    '/subcategories/{subcategory_id}',
    tags=['Subcategories'],
    response_model=SubcategoryGetSchema,
    status_code=status.HTTP_200_OK,
)
async def get_subcategory(
        subcategory_id: int,
        service: SubcategoryService = Depends()
):
    return await service.get_subcategory(subcategory_id)


@subcategory_router.post(
    '/subcategories',
    tags=['Subcategories'],
    response_model=SubcategoryGetSchema,
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
    response_model=SubcategoryGetSchema,
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
    response_model=SubcategoryGetSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_subcategory(
        subcategory_id: int,
        service: SubcategoryService = Depends()
):
    return await service.delete_subcategory(subcategory_id)
