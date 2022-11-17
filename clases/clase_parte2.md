## Dejemos de retrabajar tanto

## Creamos un CRUD base
* Debemos habilitar la edicion, busqueda y eliminacion de datos
* Recordemos
  * __model__: es un base model de sqlalchemy
  * __id_property__: es una propiedad por la que podemos buscar
  * la funcion filter recibe un parametros de busqueda, propiedades de los modelos
  * entity: es una schema
    * Agregar
    ```session.add(self.__model__(**entity.dict()))```
    * Buscar por una propiedad
    ``` session.query(self.__model__).filter(self.__id_property__ == id_entity).first() ```
    * Eliminar todas las coincidencias
    ```session.query(self.__model__).filter(self.__id_property__ == id_entity).delete()```
## Clase generica
    * en la carpeta database_sql/queries/base_queries.py

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
* asi se ve en conjunto (Usar esto solo de guia)
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

* Responder las siguientes preguntas
  * Que es un modelo?
  * Que es una schema?