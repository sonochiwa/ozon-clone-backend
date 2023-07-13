from fastapi.params import Query


class Pagination:
    def __init__(self, limit: int, offset: int):
        self.limit = limit
        self.offset = offset

    @staticmethod
    def get_pagination(
            limit: int = Query(default=None, ge=1),
            offset: int = Query(default=None, ge=1)
    ):
        return Pagination(limit, offset)
