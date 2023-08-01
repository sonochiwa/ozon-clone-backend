from fastapi import Query

from core.exceptions.server_exception import ServerException
from core.helpers.filters_helper import Filter


def add_filters(query: Query, filters: Filter, model) -> Query:
    for field_name in filters.fields.keys():
        if field_name.key not in model.__table__.columns.keys():
            raise ServerException("Неверно передано поле для фильтрации")
        else:
            query = query.where(field_name == filters.fields[field_name])
    return query
