# CURSO PYTHON
### install dependencies
 pip install -r requirements.txt
### run:
uvicorn main:app --reload

run: `docker compose up`

### Create Mysql Url

### Check Docs for [SQLAlchemy](https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqldb)
> mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
#### For us
> mysql+mysqldb://user:password@127.0.0.1/db
> 
#### Create .env or set:

```
export MYSQL_URI="mysql://user:password@127.0.0.1/db"
```
##### if you use .env:
> pip install python-dotenv

then add in your main.py in the first lines:
```
from dotenv import load_dotenv
load_dotenv()
```
### create settings.py
```
class Settings(BaseSettings):
    mysql_uri: str = os.getenv('MYSQL_URI')
```

##### set orm sqlalchemy
> pip install sqlalchemy

#### Create package database_sql
#### inside package database_sql, create a file named connection.py
```
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('SQL_URI')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```
* [For more info](https://fastapi.tiangolo.com/tutorial/sql-databases/)

#### Add to main.py
> Base.metadata.create_all(bind=engine)

This will connect with your database

#### Now Add Migrations 
