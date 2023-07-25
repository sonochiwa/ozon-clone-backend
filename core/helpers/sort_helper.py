from fastapi.params import Query

from core.enums.sort_enum import SortEnum


class Sort:
    def __init__(self, sort: SortEnum) -> None:
        self.sort = sort

    @staticmethod
    def get_sort(
            sort: SortEnum = Query(default=SortEnum.ASC),
    ):
        return sort
