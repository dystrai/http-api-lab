import csv
from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Animal(BaseModel):
    emoji: str
    english: str
    portugues: str
    nome_cientifico: str

def carrega_animais():
    try:
        leitor_animais = csv.DictReader(open('emojis-animais.csv', encoding='utf-8'))
        dic_animais = {}
        for dados_animal in leitor_animais:
            dic_animais[dados_animal['portugues']] = Animal(**dados_animal)
            
        return dic_animais
    except Exception as e:
        print('Deu erro:', e)
        

animais = carrega_animais()

@app.get("/animais/{nome_portugues}", response_model=Animal)
def obter_animal(nome_portugues: str):
    """Obtém os dados de um animal pelo nome em português"""
    animal = animais.get(nome_portugues)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal

@app.get("/animais", response_model=list[Animal])
def listar_animais():
    """Lista todos os animais disponíveis"""
    return list(animais.values())

@app.delete("/animais/{nome_portugues}", response_model=Animal)
def deletar_animal(nome_portugues: str):
    """Deleta um animal pelo nome em português"""
    animal = animais.pop(nome_portugues, None)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal

