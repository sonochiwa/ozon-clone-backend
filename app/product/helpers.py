from core.database.models.product import Product
from core.helpers.filters_helper import Filter


class ProductHelper:
    @classmethod
    def get_filter(
            cls,
            is_active: bool | None = None,
            subcategory_id: int | None = None,
    ):
        filter_field = {}

        if is_active is not None:
            filter_field[Product.is_active] = is_active

        if subcategory_id is not None:
            filter_field[Product.subcategory_id] = subcategory_id

        return Filter(filter_field)
