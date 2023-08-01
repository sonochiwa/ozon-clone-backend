from fastapi import HTTPException
from starlette import status


def add_pagination(query, pagination):
    if pagination.limit:
        if not pagination.page:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Field page is None, but must be int')
        query = query.limit(pagination.limit)

    if pagination.page:
        if not pagination.limit:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Field limit is None, but must be int')
        query = query.offset((pagination.page - 1) * pagination.limit)

    return query
