from core.database.models.subcategory import Subcategory
from core.helpers.filters_helper import Filter


class SubcategoryHelper:
    @classmethod
    def get_filter(
            cls,
            category_id: int | None = None,
    ):
        filter_field = {}

        if category_id:
            filter_field[Subcategory.category_id] = category_id

        return Filter(filter_field)
