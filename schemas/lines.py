from pydantic import BaseModel


class LinesSchema(BaseModel):
    name: str
    id_brand: int

    class Config:
        orm_model = True
