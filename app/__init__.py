from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.user.model import User
from core.config import config
from core.db.session import engine
from core.imports.import_routes import routes


def init_routers(_app: FastAPI) -> None:
    _app.include_router(routes, prefix='/api')


def create_app():
    _app = FastAPI(
        title='Ozon сlone API docs',
        docs_url=None if config.ENV == 'production' else '/docs',
    )
    _admin = Admin(_app, engine)

    class UserAdmin(ModelView, model=User):
        column_list = [User.id, User.first_name]

    _admin.add_view(UserAdmin)

    init_routers(_app)

    from starlette.middleware.cors import CORSMiddleware

    origins = [
        'http://localhost:3000'
    ]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'],
        allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'X-Total-Count'],
    )

    return _app


app = create_app()


@app.on_event("startup")
async def startup_event():
    print('INFO:     docs - http://0.0.0.0:8000/docs')


@app.on_event("shutdown")
async def shutdown_event():
    pass
