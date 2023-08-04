from pydantic import BaseModel


class ImageGetSchema(BaseModel):
    id: int
    filename: str
    size: int

    class Config:
        from_attributes = True


class ImageCreateSchema(BaseModel):
    path: str


class ImageUpdateSchema(BaseModel):
    path: str
