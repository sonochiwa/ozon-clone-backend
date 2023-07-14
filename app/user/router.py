from fastapi import APIRouter

from app.user.schema import UserReadSchema, UserCreateSchema, UserUpdateSchema
from app.user.service import fastapi_users, auth_backend

user_router = APIRouter()

user_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["Auth"])
user_router.include_router(fastapi_users.get_register_router(UserReadSchema, UserCreateSchema), prefix="/auth", tags=["Auth"])
user_router.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["Auth"])
user_router.include_router(fastapi_users.get_verify_router(UserReadSchema), prefix="/auth", tags=["Auth"])
user_router.include_router(fastapi_users.get_users_router(UserReadSchema, UserUpdateSchema), prefix="/users", tags=["Users"])

