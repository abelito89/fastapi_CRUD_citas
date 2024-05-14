"""
     API para Gestionar una Agenda:

Crea un modelo Pydantic para representar una cita con los siguientes campos:
ID (autogenerado)
Fecha
Hora
Título
Descripción
Define un endpoint para crear nuevas citas usando el modelo de Pydantic como entrada.
Crea un endpoint para recuperar una cita por su ID.
Crea un endpoint para actualizar una cita existente.
Crea un endpoint para eliminar una cita por su ID.
    """
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cita(BaseModel):
    ID: int
    Fecha: str
    Titulo: str
    Descripcion: str

class ListaDeCitas(BaseModel):
    lista: List[Cita]

cita1 = Cita(ID=1, Fecha="2024", Titulo="Gandalf" ,Descripcion="Todo lo que debes es decidir que hacer con el tiempo que se te ha dado")
lista_de_citas = []

@app.post('/crear_cita') # crea nueva cita y la agrega a la lista
async def crear_cita(cita:Cita) -> List[Cita]:
    lista_de_citas.append(cita)
    return lista_de_citas
print (lista_de_citas)

@app.get('/')
async def observar_lista() -> dict:
    return {"lista": lista_de_citas}

@app.get('/cita_por_id {id_cita}')
async def devolver_cita_segun_id(id_cita:int) -> Cita:
    for cita in lista_de_citas:
        if cita.ID == id_cita:
            return cita
    raise HTTPException(status_code=404, detail="No se ha encontrado ninguna cita con el ID proporcionado")

@app.put('/actualizar_cita/{id_cita_modificar}')
async def actualizar_cita(id_cita_modificar:int, nueva_cita:Cita) -> Cita:
    for i,cita in enumerate(lista_de_citas):
        if cita.ID == id_cita_modificar:
            lista_de_citas[i] = nueva_cita
        return lista_de_citas[i]


