from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.type_fuel import TypeFuelSchema
from services.typefuel import TypeFuelServices

router=APIRouter()
service=TypeFuelServices()

@router.post("/")
async def  create (entity:TypeFuelSchema, session=Depends (get_db)):
    return service.add(entity, session)
@router.get("/")
async def all (session=Depends (get_db)):
    return service.all(session)