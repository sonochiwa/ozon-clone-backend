from uuid import UUID

from pydantic import Field, BaseModel


class ProductReadSchema(BaseModel):
    id: UUID | None
    name: str | None = Field(None, max_length=100)
    price: float | None
    count: int | None
    discount: int | None
    views: int | None
    is_active: bool | None
    description: str | None

    subcategory_id: int | None

    class Config:
        from_attributes = True


class ProductCreateSchema(BaseModel):
    name: str = Field(..., max_length=255)
    price: float
    count: int | None = None
    discount: int | None = Field(default=0, ge=0, le=100)
    is_active: bool | None = Field(default=False)
    description: str | None = None

    subcategory_id: int


class SubcategoryUpdateSchema(BaseModel):
    name: str | None = Field(None, max_length=100)
    category_id: int | None = Field(None)
