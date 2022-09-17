from fastapi import FastAPI

app = FastAPI()


#HOLA LAUUUU
@app.get("/")
async def root():
    return {"message": "Hello World"}
