from fastapi import FastAPI, UploadFile, File
import firebase_admin
from firebase_admin import credentials, storage
from controllers import vehicle, city
from database_sql.connection import Base, engine
from models.feeling import Moto
from settings import Settings

app = FastAPI()

settings = Settings()

lista_moto: [Moto] = []

Base.metadata.create_all(bind=engine)

cred = credentials.Certificate("./files/firebase.json")
firebase_admin.initialize_app(cred)


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": settings.mysql_uri}


@app.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile = File(description="A file read as UploadFile"),
):
    read = await file.read()

    PATH =f'public/{file.filename}'
    f = open(PATH, 'wb')
    f.write(read)
    f.close()
    bucket = storage.bucket(name='roadbook-v1.appspot.com')
    blob = bucket.blob('test.png')
    blob.upload_from_filename(PATH)
    blob.make_public()
    print("your file url", blob.make_public())
    return {"filename": blob.public_url}


app.include_router(vehicle.router, prefix="/vehicle")
app.include_router(city.router, prefix="/city")
