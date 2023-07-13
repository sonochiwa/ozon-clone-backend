from starlette.middleware.cors import CORSMiddleware

from app import app

origins = [
    'http://localhost:3000/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['OPTIONS', 'GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
    allow_headers=['*'],
)
