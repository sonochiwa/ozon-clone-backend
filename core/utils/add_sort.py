from core.helpers.sort_helper import SortEnum


def add_sort(query, sort: SortEnum, model):
    if sort is SortEnum.ASC:
        query = query.order_by(model.id.asc())

    if sort is SortEnum.DESC:
        query = query.order_by(model.id.desc())

    return query
