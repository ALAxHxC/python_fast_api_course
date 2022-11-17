# CURSO PYTHON

# INSTALAR DEPENDENCIAS

`pip install -r requirements.txt`

# CORRER APP:

    `uvicorn main:app --reload`

# DESHABILITAR MYSQL AL INICIO

    `sudo systemctl disable mysql`

# CORRER DOCKER

`docker compose up`

# PARAR DOCKER

`docker compose down`

# CORRER MIGRACIONES

`alembic upgrade head`

# CREAR MIGRACION

`alembic revision --autogenerate -m "se agregan propiedades"`

# SETIAR VARIABLE DE ENTORNO

`export SQL_URI="mysql+mysqldb://user:password@127.0.0.1/db"`

# IMPORTAR POSTMAN

`https://www.getpostman.com/collections/13fc5c2443b927bbf373`

# DUDAS
 * [Como iniciar proyecto](https://youtu.be/tSQYxw0AbfE)
 * [Como obtener por id](https://youtu.be/1LcpqzNnlTM)
 * [Agregando logica de negocio](https://youtu.be/QTzbyLTDfVc)
 * [Agregando relaciones](https://youtu.be/-o0lG_yqFYI)