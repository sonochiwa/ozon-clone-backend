from fastapi.params import Query


class Pagination:
    def __init__(self, limit: int, page: int):
        self.limit = limit
        self.page = page

    @staticmethod
    def get_pagination(
            limit: int = Query(default=None, ge=1),
            page: int = Query(default=None, ge=1)
    ):
        return Pagination(limit, page)
