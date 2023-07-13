from fastapi import APIRouter

from app.category.router import category_router
from app.user.router import user_router

routes = APIRouter()

routes.include_router(user_router)
routes.include_router(category_router)
