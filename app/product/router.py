from fastapi import APIRouter, Depends, Response
from starlette import status

from app.product.helpers import ProductHelper
from app.product.schema import ProductReadSchema
from app.product.service import ProductService
from core.enums.sort_enum import SortEnum
from core.helpers.filters_helper import Filter
from core.helpers.pagination_helper import Pagination
from core.helpers.sort_helper import Sort

product_router = APIRouter()


@product_router.get(
    '/products',
    tags=['Products'],
    response_model=list[ProductReadSchema],
    status_code=status.HTTP_200_OK,
)
async def read_all_products(
        response: Response,
        pagination: Pagination = Depends(Pagination.get_pagination),
        sort: SortEnum = Depends(Sort.get_sort),
        filters: Filter = Depends(ProductHelper.get_filter),
        service: ProductService = Depends(),
):
    subcategories, total_count = await service.read_all_products(pagination, sort, filters)
    response.headers["X-Total-Count"] = total_count
    return subcategories

#
# @subcategory_router.get(
#     '/subcategories/{subcategory_id}',
#     tags=['Subcategories'],
#     response_model=SubcategoryReadSchema,
#     status_code=status.HTTP_200_OK,
# )
# async def read_subcategory(
#         subcategory_id: int,
#         service: SubcategoryService = Depends()
# ):
#     return await service.read_subcategory(subcategory_id)
#
#
# @subcategory_router.post(
#     '/subcategories',
#     tags=['Subcategories'],
#     response_model=SubcategoryReadSchema,
#     status_code=status.HTTP_201_CREATED,
# )
# async def create_subcategory(
#         request: SubcategoryCreateSchema,
#         service: SubcategoryService = Depends()
# ):
#     return await service.create_subcategory(request)
#
#
# @subcategory_router.put(
#     '/subcategories/{subcategory_id}',
#     tags=['Subcategories'],
#     response_model=SubcategoryReadSchema,
#     status_code=status.HTTP_200_OK,
# )
# async def update_subcategory(
#         request: SubcategoryUpdateSchema,
#         subcategory_id: int,
#         service: SubcategoryService = Depends()
# ):
#     return await service.update_subcategory(request, subcategory_id)
#
#
# @subcategory_router.delete(
#     '/subcategories/{subcategory_id}',
#     tags=['Subcategories'],
#     response_model=SubcategoryReadSchema,
#     status_code=status.HTTP_200_OK,
# )
# async def delete_subcategory(
#         subcategory_id: int,
#         service: SubcategoryService = Depends()
# ):
#     return await service.delete_subcategory(subcategory_id)
