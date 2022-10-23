from pydantic import BaseModel

class VehicleSchema(BaseModel):
    id: str
    name: str

    class Config:
        orm_model= True
