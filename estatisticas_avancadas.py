from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")  # Banco de dados real
client = MongoClient(mongo_uri)
db = client["candidatos"]
politico_collection = db["politicos"]
partido_collection = db["partidos"]
coligacao_collection = db["coligacoes"]

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
partido_collection = db["partidos"]
coligacao_collection = db["coligacoes"]

def porcentagem_candidaturas_por_instrucao():
    total_candidatos = politico_collection.count_documents({})
    instrucoes = {}

    for politico in politico_collection.find({}, {"_id": 0, "instrucao": 1}):
        instrucao = politico.get("instrucao", "").lower()
        if instrucao not in instrucoes:
            instrucoes[instrucao] = 0
        instrucoes[instrucao] += 1

    instrucoes_percentual = {instrucao: round((quantidade / total_candidatos) * 100, 2) for instrucao, quantidade in instrucoes.items()}
    return instrucoes_percentual

def quantidade_candidaturas_por_partido():
    partidos = {}
    
    for politico in politico_collection.find({}, {"_id": 0, "partido": 1}):
        partido_id = politico.get("partido")
        
        if partido_id:
            # Busca o nome do partido utilizando o ObjectId
            partido = partido_collection.find_one({"_id": partido_id}, {"_id": 0, "nome": 1})
            partido_nome = partido.get("nome", "Desconhecido") if partido else "Desconhecido"
        else:
            partido_nome = "Desconhecido"
        
        if partido_nome not in partidos:
            partidos[partido_nome] = 0
        partidos[partido_nome] += 1

    return partidos


def porcentagem_mulheres_candidatas():
    total_candidatos = politico_collection.count_documents({})
    mulheres_candidatas = politico_collection.count_documents({"genero": "feminino"})
    
    if total_candidatos > 0:
        porcentagem = round((mulheres_candidatas / total_candidatos) * 100, 2)
    else:
        porcentagem = 0

    return porcentagem

def porcentagem_candidaturas_por_raca():
    total_candidatos = politico_collection.count_documents({})
    racas = {}

    for politico in politico_collection.find({}, {"_id": 0, "raca": 1}):
        raca = politico.get("raca", "").lower()
        if raca not in racas:
            racas[raca] = 0
        racas[raca] += 1

    racas_percentual = {raca: round((quantidade / total_candidatos) * 100, 2) for raca, quantidade in racas.items()}
    return racas_percentual


# Testando as funções

# print("\n################ TESTE COM Quantidade de Candidaturas por Partido ############")
# resultado_partido = quantidade_candidaturas_por_partido()
# print(resultado_partido)

# print("\n################ TESTE COM Porcentagem de Mulheres Candidatas ############")
# resultado_mulheres = porcentagem_mulheres_candidatas()
# print(f"Porcentagem de Mulheres: {resultado_mulheres:.2f}%")

# print("\n################ TESTE COM Porcentagem de Candidaturas por Raça ############")
# resultado_raca = porcentagem_candidaturas_por_raca()
# print(resultado_raca)

# print("\n################ TESTE COM Porcentagem de Candidaturas por Instrução ############")
# resultado_instrucao = porcentagem_candidaturas_por_instrucao()
# print(resultado_instrucao)