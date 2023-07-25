from fastapi import HTTPException
from starlette import status


def add_pagination(query, pagination):
    if pagination.limit:
        if not pagination.offset:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Field offset is None, but must be int')
        query = query.limit(pagination.limit)

    if pagination.offset:
        if not pagination.limit:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Field limit is None, but must be int')
        query = query.offset((pagination.offset - 1) * pagination.limit)

    return query
