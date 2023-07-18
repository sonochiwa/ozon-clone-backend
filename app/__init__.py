from fastapi import FastAPI

from app.user.model import User
from core.config import config
from core.fastapi.middlewares.cors import init_cors
from core.imports.import_routes import routes


def init_routers(_app: FastAPI) -> None:
    _app.include_router(routes, prefix='/api')


def create_app():
    _app = FastAPI(
        title='Ozon clone API docs',
        docs_url=None if config.ENV == 'production' else '/docs',
    )
    init_cors(_app)
    init_routers(_app)

    # admin = Admin(_app, engine)
    #
    # class UserAdmin(ModelView, model=User):
    #     column_list = [User.id, User.first_name]
    #
    # admin.add_view(UserAdmin)

    return _app


app = create_app()


@app.on_event("startup")
async def startup_event():
    print(f'INFO:     docs - http://{config.APP_HOST}:{config.APP_PORT}/docs')


@app.on_event("shutdown")
async def shutdown_event():
    pass
