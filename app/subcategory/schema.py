from pydantic import Field, BaseModel


class SubcategoryReadSchema(BaseModel):
    id: int | None
    name: str | None = Field(None, max_length=100)
    category_id: int | None = Field(None)

    class Config:
        from_attributes = True


class SubcategoryCreateSchema(BaseModel):
    name: str = Field(..., max_length=100)
    category_id: int = Field(...)


class SubcategoryUpdateSchema(BaseModel):
    name: str | None = Field(None, max_length=100)
    category_id: int | None = Field(None)
