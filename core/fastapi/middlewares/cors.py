from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

origins = [
    'http://localhost:3000',
]


def init_cors(_app: FastAPI) -> None:
    return _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['OPTIONS', 'GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
        allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'X-Total-Count'],
        expose_headers=['X-Total-Count'],
    )
