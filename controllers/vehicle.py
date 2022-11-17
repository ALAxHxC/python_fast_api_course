from fastapi import APIRouter, Depends
from database_sql.connection import get_db
from schemas.vehicle import VehicleSchema
from services.vehicle import VehicleService

router = APIRouter()
service = VehicleService()


@router.post("/", tags=["vehicle"])
async def create(entity: VehicleSchema, session=Depends(get_db)):
    return entity
