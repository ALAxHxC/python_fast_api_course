from fastapi import APIRouter, Depends

from database_sql.connection import get_db
from schemas.actions import ActionsSchema
from services.actions import ActionsServices

router=APIRouter()
service=ActionsServices()

@router.post("/")
async def  create (entity:ActionsSchema, session=Depends (get_db)):
    return service.add(entity, session)
@router.get("/")
async def all (session=Depends (get_db)):
    return service.all(session)
