from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database_sql.queries.vehicule_queries import VehicleQueries
from schemas.vehicle import VehicleSchema
from services.base_services import BaseServices
from services.cities import CitiesServices

queries = VehicleQueries()
city_services = CitiesServices()


class VehicleService(BaseServices):
    def get(self, session: Session, id_entity):
        return queries.get_by_id(session, id_entity)
        pass

    def add(self, session: Session, entity: VehicleSchema):
        city = city_services.get_by_id(session, entity.city_data)
        if city is None:
            raise HTTPException(status_code=404, detail="City not found")
        return queries.create(session, entity)

    def search(self, session: Session, limit, skip):
        return queries.all_data(session)

    def delete(self, session: Session, id_entity):
        pass

    def update(self, session: Session, id_entity, entity: BaseModel):
        pass

    def partial_update(self, session: Session, id_entity, params_to_update: dict):
        pass
