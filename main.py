from fastapi import FastAPI
from pydantic import BaseModel


"""
para rodar vscode
pip install --user fastapi uvicorn  
pip install basemodel
python -m uvicorn main:app --reload
"""

app = FastAPI()

contatos = list()

class Contato(BaseModel):
    name: str
    num: int


@app.get("/")
def root():
    return contatos


@app.get("/contatos/{name}")
def get_contato(name: str):
    for i in contatos:
        if i.name  == name:
            return i
    else:
        return None


@app.post("/adicionar/")
def criar_contato(contato: Contato):
    contatos.append(contato)
    return contatos

@app.delete("/deletar/{name}")
def deletar_contato(name: str):
    for i in contatos:
        if i.name  == name:
            return contatos.remove(i)
        else:
            return None
    
@app.put("/alterar/{name}/{num}")
def alterar_contato(name: str):
    for i in contatos:
        if i.name  == name:
            return contatos
        else:
            return None
""" 
    tarefas[pos].feito = True
    return tarefas[pos] """