# Hi Laura, have a great day!, 
#### You forgot any command? remember you can find here

* To set envrioment for sql:
> export SQL_URI="mysql+mysqldb://user:password@127.0.0.1/db"
* To start docker
> docker compose up
* To stop docker
> docker compose down
* to start app:
> uvicorn main:app --reload
* migration
> alembic revision --autogenerate -m "actionmodel"
* run migration
> alembic upgrade head  