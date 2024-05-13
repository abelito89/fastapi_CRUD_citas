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
from fastapi import FastAPI
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

cita1 = Cita(ID=1, Fecha="2024", Titulo="Gandalf" ,Descripcion="Todo lo que tienes que hacer es que hacer con el tiempo que se te ha dado")
lista_de_citas = []

@app.post('/crear_cita')
async def crear_cita(cita:Cita) -> List[Cita]:
    lista_de_citas.append(cita)
    return lista_de_citas
print (lista_de_citas)
@app.get('/')
async def observar_lista() -> dict:
    return {"lista": lista_de_citas} 

