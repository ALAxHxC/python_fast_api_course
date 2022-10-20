import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    sql_uri: str = os.getenv('SQL_URI')
