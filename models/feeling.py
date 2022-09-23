from pydantic import BaseModel
class Transporte:
    def __init__(self,vehiculo,tipo):
        self.vehiculo=vehiculo
        self.tipo=tipo
    vehiculo:str
    tipo: str

class Moto(BaseModel):
    name: str
    description: str
    brand: str
    cc:int
    abs: bool= False




