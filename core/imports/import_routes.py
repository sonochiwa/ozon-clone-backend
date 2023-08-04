from fastapi import APIRouter

from app.category.router import category_router
from app.image.router import image_router
from app.product.router import product_router
from app.subcategory.router import subcategory_router
from app.user.router import user_router

routes = APIRouter()

routes.include_router(user_router)
routes.include_router(category_router)
routes.include_router(subcategory_router)
routes.include_router(product_router)
routes.include_router(image_router)
