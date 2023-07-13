from pydantic import Field, BaseModel


class CategoryRead(BaseModel):
    id: int | None
    name: str | None = Field(None, max_length=100)

    class Config:
        from_attributes = True


class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=100)


class CategoryUpdate(BaseModel):
    name: str = Field(..., max_length=100)
