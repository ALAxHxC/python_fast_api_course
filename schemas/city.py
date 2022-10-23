from pydantic import BaseModel


class CitySchema(BaseModel):
    id: int
    name: str
    country: str

    class Config:
        orm_model = True
