from fastapi import Request, FastAPI, HTTPException

app = FastAPI()


lista_sentimientos = []

#HOLA LAUUUU
@app.get("/")
async def root():
    return {"message": lista_sentimientos}

@app.post("/")
async def add(request: Request):
    persons = await request.json()
    for emocion in lista_sentimientos:
        if persons.get('feeling')==emocion.get('feeling') and persons.get('name')==emocion.get('name'):
            raise HTTPException(status_code=400, detail="Feeling for that person already exists")

    lista_sentimientos.append(await request.json())

    return lista_sentimientos

@app.put("/")
async def update(request: Request):
    persona = await request.json()
    for emocion in lista_sentimientos:
        if persona.get("name")== emocion.get("name"):
            emocion["feeling"]=persona.get("feeling")
    return lista_sentimientos

