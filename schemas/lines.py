from pydantic import BaseModel

class LinesSchema(BaseModel):
    name:str
    class Config:
        orm_model= True