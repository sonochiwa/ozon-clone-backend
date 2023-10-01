from pydantic import Field, BaseModel


class CategoryGetSchema(BaseModel):
    id: int | None
    name: str | None = Field(None, max_length=100)
    slug: str | None = Field(None, max_length=255)
    image_id: int | None = Field(None)

    class Config:
        from_attributes = True


class CategoryCreateSchema(BaseModel):
    name: str = Field(..., max_length=100)
    image_id: int | None = None


class CategoryUpdateSchema(BaseModel):
    name: str | None = Field(None, max_length=100)
    image_id: int | None = None
