from pydantic import BaseModel


class ImageGetSchema(BaseModel):
    id: int | None
    path: str | None

    class Config:
        from_attributes = True


class ImageCreateSchema(BaseModel):
    path: str


class ImageUpdateSchema(BaseModel):
    path: str
