from fastapi import FastAPI

from controllers import vehicle, city
from database_sql.connection import Base, engine
from models.feeling import Moto
from settings import Settings

app = FastAPI()

settings= Settings()

lista_moto: [Moto] = []

Base.metadata.create_all(bind=engine)


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": settings.mysql_uri}

app.include_router(vehicle.router, prefix="/vehicle")
app.include_router(city.router, prefix="/city")