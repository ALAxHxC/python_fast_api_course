from fastapi import Request, FastAPI, HTTPException
from controllers import vehicle, cities
from database_sql.connection import Base, engine
from settings import Settings


app = FastAPI()

settings= Settings()


Base.metadata.create_all(bind=engine)


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": settings.mysql_uri}

app.include_router(vehicle.router, prefix="/vehicle")
app.include_router(cities.router, prefix="/cities")