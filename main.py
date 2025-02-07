from fastapi import FastAPI
from pydantic import BaseModel

"""
para rodar vscode
pip install --user fastapi uvicorn  
pip install pydantic
python -m uvicorn main:app --reload
py -m uvicorn main:app --reload
"""
"""
http://localhost:8000/
http://localhost:8000/docs
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
    
@app.put("/alterar-numero/{name}/{num}")
def alterar_numero(name: str, num:int):
    for i in contatos:
        if i.name == name:
            i.num = num
    return None

@app.put("/alterar-nome/{num}/{name}")
def alterar_nome(name: str, num:int):
    for i in contatos:
        if i.num == num:
            i.name = name
    return None

@app.get("/lista")
def lista():
    return contatos