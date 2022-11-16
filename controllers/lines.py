from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.lines import LinesSchema
from services.lines import LinesServices

router=APIRouter()
service=LinesServices()

@router.post("/")
async def  create (entity:LinesSchema, session=Depends (get_db)):
    return service.add(entity, session)
@router.get("/")
async def all (session=Depends (get_db)):
    return service.all(session)