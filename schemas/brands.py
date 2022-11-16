from pydantic import BaseModel

class BrandsSchema(BaseModel):
    id_runt: int
    description: str
    class Config:
        orm_model= True