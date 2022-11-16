from fastapi import Request, FastAPI, HTTPException
from controllers import vehicle, cities, actions, brands, lines, typefuel
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
app.include_router(actions.router, prefix="/actions")
app.include_router(brands.router, prefix="/brands")
app.include_router(lines.router, prefix="/lines")
app.include_router(typefuel.router, prefix="/typefuel")


