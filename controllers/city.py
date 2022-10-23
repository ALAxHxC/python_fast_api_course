from fastapi import APIRouter, Depends

from database_sql.connection import get_db
from schemas.city import CitySchema
from services.city import CityServices

router = APIRouter()
service = CityServices()


@router.post("/", tags=["city"])
async def create(entity: CitySchema, session=Depends(get_db)):
    return service.add(entity, session)

@router.get("/", tags=["city"])
async def all(session=Depends(get_db)):
    return service.all(session)

@router.delete("/{id}", tags=["city"])
async def delete(id,session=Depends(get_db)):
    return service.remove(id,session)

