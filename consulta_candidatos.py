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

def consultar_candidatos(nome=None, idade=None, raca=None, genero=None, ocupacao=None, candidatura=None, localizacao=None, partido_nome=None):
    politicos_encontrados = []  
    
    for politico in politico_collection.find({}, {"_id": 0}):
        if nome and not safe_lower(politico.get("nome", "")).startswith(nome.lower()):
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
            
        if localizacao and localizacao.lower() not in politico.get("cidade", "").lower():
            continue

        # Filtro por partido
        if partido_nome and partido_nome.lower() not in politico["partido"].lower():
            continue
        
        politicos_encontrados.append(politico)
    
    return politicos_encontrados

def _calcular_ano_nascimento(idade):
    ano_atual = datetime.now()
    ano_nascimento = ano_atual.year - idade
    
    if (ano_atual.month, ano_atual.day) < (1, 1):
        ano_nascimento -= 1
    return ano_nascimento

def safe_lower(value):
    return value.lower() if isinstance(value, str) else ""

def listar_partidos():
    partidos = []
    for partido in partido_collection.find({}, {"_id": 0}):  # Projeta para excluir o campo _id
        partidos.append(partido)  # Adiciona cada partido à lista
    return partidos

def listar_cargos():
    cargos = politico_collection.distinct("cargo")
    return cargos

def listar_cidades():
    cidades = politico_collection.distinct("cidade")
    return cidades

def listar_raca():
    racas = politico_collection.distinct("raca")
    return racas

def listar_genero():
    generos = politico_collection.distinct("genero")
    return generos

def listar_ocupacao():
    ocupacoes = politico_collection.distinct("ocupacao")
    return ocupacoes

# Testes
# print("################ TESTE COM NOME ############ ")
'''resultado = consultar_candidatos(nome="jose carlos pedreiro")
for info in resultado:
    texto_info = f"Nome: {info['nome']}\nRaça: {info['raca']}\nGênero: {info['genero']}\nNascimento: {info['nascimento']}\n" \
                 f"Estado: {info['estado']}\nCidade: {info['cidade']}\nInstrução: {info['instrucao']}\n" \
                 f"Cargo: {info['cargo']}\nOcupação: {info['ocupacao']}\nPartido: {info['partido']}\nColigação: {info['coligacao']}\n\n"

    print(texto_info)   
'''
    
# print("################ TESTE COM NOME + idade ############ ")
# resultados = consultar_candidatos(idade=59, raca="preta", nome="nego ")
# print(resultados)  # Espera-se que retorne todos os dados de "Nelson"

# print("\n\n\n################ TESTE COM NOME + RACA ############ ")
# resultados = consultar_candidatos(nome="nelson", raca="branca")
# print(resultados)  


# #  # Teste com idade
# print("\n\n\n################ TESTE COM NOME + IDADE ############ ")
# resultados = consultar_candidatos(nome="nelson ", idade=59)
# print(resultados) 

# ##  Teste com gênero
# print("\n\n\n################ TESTE COM GENERO ############ ")
# resultados = consultar_candidatos(genero="Feminino")
# print(len(resultados))  

# # Teste com cargo
# print("\n\n\n################ TESTE COM CARGO ############ ")
# resultados = consultar_candidatos(nome="ana", candidatura="vereador")
# print(len(resultados))  # Espera-se que retorne candidatos com o cargo "vereador"
