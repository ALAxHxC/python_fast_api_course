from datetime import datetime

from pydantic import BaseModel


class VehicleSchema(BaseModel):
    id: str = None
    name: str
    city_data: int
    brand: str
    line: str
    type_fuel: int
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_model = True
