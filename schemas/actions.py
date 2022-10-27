from pydantic import BaseModel

class ActionsSchema(BaseModel):
    description: str
    medida: str

    class Config:
        orm_model= True

