# Empecemos a jugar
* Vamos a guardar los vehiculos para eso queremos saber:
  * marca
  * año de lanzamiento
  * nombre
  * tipo de vehiculo
  * tipo de combustible
  
  * recordemos para una relacion:
      * [Que es una llave foranea](https://es.wikipedia.org/wiki/Clave_for%C3%A1nea)
      * Recordemos un poco SQL
      * ```country_id = Column(Integer, ForeignKey("Nombre de la columna.llave primaria"), nullable=False, name="nombre_columna")```
      * ``` relationship("Nombre modelo", backref="referencia")```
      * un ejemplo
      * el tipo de variable debe ser la misma, si la llave primaria es Integer, la relation es Integer
    ```
    country_id = Column(Integer, ForeignKey("admin_pais.admin_id_pais"), nullable=False, name="admin_id_pais")
    country = relationship("AdminMovoPais", backref="admin_id_pais_country")
    ```
* Como se vera el modelo?

```
class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), unique=True, index=True)
    # UN CONSEJO ES AGREGARLE EL NOMBRE DE LA COLUMNA
    city_data = Column(Integer, ForeignKey("cities.cod_name"), name="city")
    # CUANDO TENEMOS UNA TABLE CON VARIAS LLAVES PRIMARIAS
    brand = Column(String(45), ForeignKey("brands.id_runt"))
    line = Column(String(45), ForeignKey("lines.name"))
    type_fuel = Column(Integer, ForeignKey("type_fuel.id"))
    # CAMPOS DE TRAZABILIDAD
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

```

* Usando los genericos vamos a crear la queries para Vehiculos
HINT: Algo se me paso aqui?
* Tambien podemos volver genericos los servicios?
* Que es un clase generica
```

from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy.orm import Session


class BaseServices(ABC):
    @abstractmethod
    def add(self, session: Session,entity: BaseModel):
        pass

    @abstractmethod
    def search(self,session: Session, limit, skip):
        pass

    @abstractmethod
    def delete(self,session: Session, id_entity):
        pass

    @abstractmethod
    def update(self, session: Session, id_entity, entity: BaseModel):
        pass

    @abstractmethod
    def partial_update(self, session: Session, id_entity, params_to_update: dict):
        pass
```
* la heradamos y eso nos hace implementar los metodos
```
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database_sql.queries.vehicule_queries import VehicleQueries
from services.base_services import BaseServices

queries = VehicleQueries()


class VehicleService(BaseServices):
    def get(self, session: Session, id_entity):
        return queries.get_by_id(session, id_entity)
        pass

    def add(self, session: Session, entity: BaseModel):
        return queries.create(session, entity)

    def search(self, session: Session, limit, skip):
        return queries.all_data(session)

    def delete(self, session: Session, id_entity):
        pass

    def update(self, session: Session, id_entity, entity: BaseModel):
        pass

    def partial_update(self, session: Session, id_entity, params_to_update: dict):
        pass
```
* actualizamos el controlador
```
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
```
* creamos un vehiculos
```
curl --location --request POST 'http://127.0.0.1:8000/vehicle' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"XRE300",
    "brand":1,
    "city_data":1,
    "line":"XRE300",
    "type_fuel":1
}'
```
* porque falla?
* agregemos validaciones
* revisamos la ciudad
```
class CitiesServices:
    query = CityQueries()

    def add(self, city: CitiesSchema, session: Session):
        return self.query.add(city, session)

    def all(self, session: Session):
        return self.query.all(session)

    def get_by_id(self, session: Session, id_city: int):
        return self.query.get_by_id(session, id_city)
```
 y lo agregamos en vehiculo
 
```
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

```