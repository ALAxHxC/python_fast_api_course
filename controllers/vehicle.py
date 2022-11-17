from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.vehicle import VehicleSchema
from services.vehicle import VehicleService

router = APIRouter()
service = VehicleService()


@router.post("/", tags=["vehicle"])
async def create(entity: VehicleSchema, session=Depends(get_db)):
    return service.add(session, entity)


@router.get("/", tags=["vehicle"])
async def create(session=Depends(get_db)):
    return service.search(session, 10, 0)


@router.get("/{id_entity}", tags=["vehicle"])
async def create(id_entity: int, session=Depends(get_db)):
    return service.get(session, id_entity)


@router.delete("/{id_entity}", tags=["vehicle"])
async def create(entity: int, session=Depends(get_db)):
    return service.delete(session, entity)
