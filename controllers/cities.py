from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.cities import CitiesSchema
from schemas.vehicle import VehicleSchema
from services.cities import CitiesServices
from services.vehicle import VehicleService

router = APIRouter()
service = CitiesServices()


@router.post("/", tags=["cities"])
async def create(entity: CitiesSchema, session=Depends(get_db)):
    return service.add(entity, session)


@router.get("/", tags=["cities"])
async def all(session=Depends(get_db)):
    return service.all(session)


@router.get("/name/{name}")
async def get_by_name(name: str, session=Depends(get_db)):
    return service.get_by_name(session, name)
