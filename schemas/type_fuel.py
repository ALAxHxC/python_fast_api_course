from pydantic import BaseModel

class TypeFuelSchema(BaseModel):
    description:str
    class Config:
        orm_model= True