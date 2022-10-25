from pydantic import BaseModel


class CitiesSchema(BaseModel):
    name: str
    country: str
    cod_name: int

    class Config:
        orm_model= True
