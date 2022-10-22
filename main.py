from fastapi import Request, FastAPI, HTTPException
from controllers import vehicle
from database_sql.connection import Base, engine
from settings import Settings
from models.feeling import Moto

app = FastAPI()

settings= Settings()

lista_moto: [Moto] = []

Base.metadata.create_all(bind=engine)


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": settings.mysql_uri}

app.include_router(vehicle.router, prefix="/vehicle")