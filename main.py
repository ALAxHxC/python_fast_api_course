from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from database_sql.connection import Base, engine
from settings import Settings

app = FastAPI()
settings = Settings()
Base.metadata.create_all(bind=engine)


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": settings.sql_uri}
