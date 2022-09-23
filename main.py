from fastapi import Request, FastAPI, HTTPException

from models.feeling import Moto

app = FastAPI()

lista_moto: [Moto] = []


# HOLA LAUUUU
@app.get("/")
async def rooto():
    return {"message": lista_moto}

@app.get("/no_abs")
async def noabs():
    result = map(lambda item: {
        "nombre": item.name
    }, lista_moto)
    print(result)
    return list(result)

@app.get("/{name}")
async def root(name):
    result = filter(lambda item: item.name == name, lista_moto)
    print(result)
    return list(result)


@app.post("/")
async def add(moto: Moto):
    lista_moto.append(moto)
    return lista_moto


@app.put("/{name}")
async def update(name, moto: Moto):
    print(name)
    for item in lista_moto:
        if item.name == name:
            item = moto
            return item

    raise HTTPException(status_code=400, detail="NO SE ENCUENTRA EN LA LISTA")
