from uuid import UUID

from pydantic import Field, BaseModel


class ProductReadSchema(BaseModel):
    id: UUID | None
    name: str | None = Field(None, max_length=100)
    price: float | None = Field(None)
    count: int | None = Field(None)
    discount: int | None = Field(None)
    views: int | None = Field(None)
    is_active: bool | None = Field(None)
    description: str | None = Field(None)

    subcategory_id: int | None = Field(None)

    class Config:
        from_attributes = True


class SubcategoryCreateSchema(BaseModel):
    name: str = Field(..., max_length=100)
    category_id: int = Field(...)


class SubcategoryUpdateSchema(BaseModel):
    name: str | None = Field(None, max_length=100)
    category_id: int | None = Field(None)
