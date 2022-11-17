## Scenario

1) Un desarrollador hizo cambios en el codigo, para optimizarlo y mejorar reglas, esto implica que debemos cargar nuevamente la base de datos
   * cuales son las tablas existentes?
   * en mysql worbench ejecutamos
   ```
   use db;
   show tables;
    ```
   * borramos la base de datos
   ````
    drop database db;
    create database db;
   ````
   * volvemos a correr las migraciones
   `alembic upgrade head`
   * Cuales son las nuevas tablas?
   * Estuviste de acuerdo con los cambios?
   * que harias de diferente?
   * que se puede mejorar?
   
2) Habilitamos la edicion, busqueda por id y eliminacion
   * Recordemos que para ejecutar queries nesecitamos:
     * un Model (De SQLALCHEMY)
     * Una Schema (Modelo de negocio)
     * Una propiedad por la cual buscar
   
3) Cargar CSV's
   1) vamos a cargar el de ciudades
      1) 
4) empezamos a crear el modelo de vehiculo
   1) deseamos saber
      1) marca
      2) linea
      3) fecha de lanzamiento
      4) tipo de combustible
   
5) empezamos a crear el nuevo modelo de usuario-vehiculo
   1) deseamos saber
      1) matricula
      2) ciudad
      3) usuario
      4) 
    

## Crear un query generico
* explicar: variables privada y publicas 
  * `__variable__` vs `variable`
* valores por defecto 
  * el modelo
  * la schema
  * el id unico
```
class BaseQueries:
    __model__ = None
    __schema__ = None
    __id_property__ = None
```
* constructor
  * que es un constructor?
```
def __init__(self, model: Base, schema, id_property) -> None:
        self.__schema__ = schema
        self.__model__ = model
        self.__id_property__ = id_property
```
* ahora las funciones bases
  * crear 
```

    def create(self, session: Session, entity: BaseModel):
        try:
            session.add(self.__model__(**entity.dict()))
            session.commit()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
```
 * obtener por su propiedad principal
```

  def get_by_id(self, session: Session, id_entity):
        print(id_entity,self.__id_property__ )
        return session.query(self.__model__).filter(self.__id_property__ == id_entity).first()
```
* obtener todos
```
 def all_data(self, session: Session):
        return session.query(self.__model__).all()
```
* actualizar 
```
  def update(self, session: Session, data: dict, id_entity):
        update_sql = update(self.__model__) \
            .where(self.__id_property__ == id_entity) \
            .values(**data)
        session.execute(update_sql)
        session.commit()
        return self.get_by_id(session, id_entity)

```
* eliminar
```
 def delete(self, session: Session, id_entity):
        session.query(self.__model__).filter(self.__id_property__ == id_entity).delete()
        session.commit()
```
* asi se ve en conjunto
```
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database_sql.connection import Base


class BaseQueries:
    __model__ = None
    __schema__ = None
    __id_property__ = None

    def __init__(self, model: Base, schema, id_property) -> None:
        self.__schema__ = schema
        self.__model__ = model
        self.__id_property__ = id_property

    def create(self, session: Session, entity: BaseModel):
        try:
            session.add(self.__model__(**entity.dict()))
            session.commit()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_by_id(self, session: Session, id_entity):
        print(id_entity,self.__id_property__ )
        return session.query(self.__model__).filter(self.__id_property__ == id_entity).first()

    def all_data(self, session: Session):
        return session.query(self.__model__).all()

    def delete(self, session: Session, id_entity):
        session.query(self.__model__).filter(self.__id_property__ == id_entity).delete()
        session.commit()

    def update(self, session: Session, data: dict, id_entity):
        update_sql = update(self.__model__) \
            .where(self.__id_property__ == id_entity) \
            .values(**data)
        session.execute(update_sql)
        session.commit()
        return self.get_by_id(session, id_entity)

```