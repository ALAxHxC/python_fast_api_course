from schemas.vehicle import VehicleSchema

class VehicleService:
    def add(self, vehicle: VehicleSchema):
        return vehicle