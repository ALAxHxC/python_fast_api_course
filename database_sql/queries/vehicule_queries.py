from database_sql.models import Vehicle
from database_sql.queries.base_queries import BaseQueries
from schemas.vehicle import VehicleSchema


class VehicleQueries(BaseQueries):
    def __init__(self):
        super().__init__(Vehicle, VehicleSchema, Vehicle.id)

    