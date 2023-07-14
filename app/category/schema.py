from pydantic import Field, BaseModel


class CategoryReadSchema(BaseModel):
    id: int | None
    name: str | None = Field(None, max_length=100)

    class Config:
        from_attributes = True


class CategoryCreateSchema(BaseModel):
    name: str = Field(..., max_length=100)


class CategoryUpdateSchema(BaseModel):
    name: str = Field(..., max_length=100)
