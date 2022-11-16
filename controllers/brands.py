from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.brands import BrandsSchema
from services.brands import BrandsServices

router=APIRouter()
service=BrandsServices()

@router.post("/")
async def  create (entity:BrandsSchema, session=Depends (get_db)):
    return service.add(entity, session)
@router.get("/")
async def all (session=Depends (get_db)):
    return service.all(session)
