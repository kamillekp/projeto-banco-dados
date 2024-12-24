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

def consultar_candidatos(nome=None, idade=None, raca=None, genero=None, ocupacao=None, candidatura=None):
    politicos_encontrados = []  
    
    for politico in politico_collection.find({}, {"_id": 0}):
        if nome and not politico["nome"].lower().startswith(nome.lower()):
            continue

        if idade:
            ano_nascimento = _calcular_ano_nascimento(idade)
            if not (ano_nascimento <= politico["nascimento"].year < ano_nascimento + 1):
                continue

        if raca and raca.lower() not in politico.get("raca", "").lower():
            continue

        if genero and genero.lower() not in politico.get("genero", "").lower():
            continue

        if ocupacao and ocupacao.lower() not in politico.get("ocupacao", "").lower():
            continue

        if candidatura and candidatura.lower() not in politico.get("cargo", "").lower():
            continue 

        partido = partido_collection.find_one({"_id": politico["partido"]}, {"_id": 0})
        if partido:
            politico["partido"] = partido.get("nome", "Desconhecido")

        coligacao = coligacao_collection.find_one({"_id": politico["coligacao"]}, {"_id": 0})
        if coligacao:
            politico["coligacao"] = coligacao.get("nome", "Desconhecido")
        
        if isinstance(politico["nascimento"], datetime):
            politico["nascimento"] = politico["nascimento"].strftime("%d/%m/%Y")
        
        politicos_encontrados.append(politico)
    
    return politicos_encontrados

def _calcular_ano_nascimento(idade):
    ano_atual = datetime.now()
    ano_nascimento = ano_atual.year - idade
    
    if (ano_atual.month, ano_atual.day) < (1, 1):
        ano_nascimento -= 1
    return ano_nascimento


def porcentagem_candidaturas_por_instrucao(politicos):
    total_candidatos = len(politicos)
    instrucoes = {}

    for politico in politicos:
        instrucao = politico["instrucao"].lower()
        if instrucao not in instrucoes:
            instrucoes[instrucao] = 0
        instrucoes[instrucao] += 1

    instrucoes_percentual = {instrucao: (quantidade / total_candidatos) * 100 for instrucao, quantidade in instrucoes.items()}
    return instrucoes_percentual


def quantidade_candidaturas_por_partido():
    partidos = {}
    
    for politico in politico_collection.find({}, {"_id": 0}):
        partido = partido_collection.find_one({"_id": politico["partido"]}, {"_id": 0})
        partido_nome = partido.get("nome", "Desconhecido") if partido else "Desconhecido"
        
        if partido_nome not in partidos:
            partidos[partido_nome] = 0
        partidos[partido_nome] += 1

    return partidos

def porcentagem_mulheres_candidatas(politicos):
    total_candidatos = len(politicos)
    mulheres = sum(1 for politico in politicos if politico["genero"].lower() == "feminino")
    porcentagem_mulheres = (mulheres / total_candidatos) * 100 if total_candidatos > 0 else 0
    return porcentagem_mulheres

print("################ TESTE COM Quantidade partido ############ ")
resultados =  quantidade_candidaturas_por_partido()
print(resultados)  # Espera-se que retorne todos os dados

# Teste com nome
print("################ TESTE COM NOME ############ ")
resultados = consultar_candidatos(nome="nelson ")
print(resultados)  # Espera-se que retorne todos os dados de "Nelson"

# Teste com idade
print("\n\n\n################ TESTE COM NOME + IDADE ############ ")
resultados = consultar_candidatos(nome="nelson ", idade=59)
print(resultados)  # Espera-se que retorne candidatos com idade aproximada de 39 anos

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
