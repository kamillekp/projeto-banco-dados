from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

# Conectar ao banco de dados MongoDB

mongo_uri = os.getenv("MONGO_URI")  # Banco de dados real
client = MongoClient(mongo_uri)
db = client["candidatos"]
politico_collection = db["politicos"]

def consultar_candidatos(nome=None, idade=None, raca=None, genero=None, ocupacao=None, candidatura=None):
    politicos_encontrados = []  
    
    for politico in politico_collection.find({}, {"_id": 0}):
        if nome and not politico["nome"].lower().startswith(nome.lower()):
            continue

        if idade:
            ano_nascimento = _calcular_ano_nascimento(idade)
            if not (ano_nascimento <= politico["nascimento"].year < ano_nascimento + 1):
                continue

        if raca and raca.lower() not in politico["raca"].lower():
            continue

        if genero and genero.lower() not in politico["genero"].lower():
            continue

        if ocupacao and ocupacao.lower() not in politico["ocupacao"].lower():
            continue

        if candidatura and candidatura.lower() not in politico["cargo"].lower():
            continue 

        # Se todos os filtros forem atendidos, adicionar o documento completo à lista de resultados
        politicos_encontrados.append(politico)
    
    return politicos_encontrados

def _calcular_ano_nascimento(idade):
    ano_atual = datetime.now().year
    return ano_atual - idade


# Supondo que o banco de dados esteja configurado corretamente

# # Teste com nome
# print("################ TESTE COM NOME ############ ")
# resultados = consultar_candidatos(nome="nelson ")
# print(resultados)  # Espera-se que retorne todos os dados de "Nelson"

# # Teste com idade
# print("\n\n\n################ TESTE COM NOME + IDADE ############ ")
# resultados = consultar_candidatos(nome="nelson ", idade=59)
# print(resultados)  # Espera-se que retorne candidatos com idade aproximada de 39 anos

# # Teste com raça
# print("\n\n\n################ TESTE COM NOME + RACA ############ ")
# resultados = consultar_candidatos(nome ="nelson felix", raca="Preta")
# print(resultados)  # Espera-se que retorne candidatos com raça "Preta"

# # Teste com gênero
# resultados = consultar_candidatos(genero="Feminino")
# print(resultados)  # Espera-se que retorne todos os candidatos do gênero feminino

# # Teste com cargo
# resultados = consultar_candidatos(candidatura="Deputada")
# print(resultados)  # Espera-se que retorne candidatos com o cargo "Deputada"
