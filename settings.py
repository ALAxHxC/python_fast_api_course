import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    mysql_uri: str = os.getenv('SQL_URI')

