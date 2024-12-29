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
cidade_collection = db["cidades"]

def consultar_candidatos(nome=None, idade=None, raca=None, genero=None, ocupacao=None, candidatura=None, estado=None, cidade=None, partido_nome=None):

    query = {}
    if nome:
        query['nome'] = { "$regex": nome.lower()}

    if idade:
        data_inicial, data_final = _calcular_anos_nascimento(int(idade))
        query['nascimento'] = { "$gte":data_inicial,"$lt":data_final}

    if raca and not raca.startswith("Selecione"):
        query['raca'] = raca.lower()

    if genero and not genero.startswith("Selecione"):
        query['genero'] = genero.lower()

    if ocupacao and not ocupacao.startswith("Selecione"):
        query['ocupacao'] = ocupacao.lower()

    if candidatura and not candidatura.startswith("Selecione"):
        query['cargo'] = candidatura.lower() 

    if estado and not estado.startswith("Selecione"):
        query['estado'] = estado.lower() 

    if cidade and not cidade.startswith("Selecione"):
        query['cidade'] = cidade.lower() 
        
    if partido_nome and not partido_nome.startswith("Selecione"):
        partido = partido_collection.find_one({"nome": partido_nome})
        query["partido"] = partido.get("_id", "")
    
    print (query)
    return politico_collection.find(query)
    
def consultar_candidatos2(nome=None, idade=None, raca=None, genero=None, ocupacao=None, candidatura=None, estado=None, localizacao=None, partido_nome=None):
    politicos_encontrados = []  
    
    for politico in politico_collection.find({}, {"_id": 0}):
        if nome and not safe_lower(politico.get("nome", "")).startswith(nome.lower()):
            continue

        if idade:
            ano_nascimento = _calcular_anos_nascimento(idade)
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

def _calcular_anos_nascimento(idade):
    data_atual = datetime.now()
    ano_nascimento = data_atual.year - idade

    start = datetime(ano_nascimento-1, data_atual.month, data_atual.day, 23, 59, 59)
    end = datetime(ano_nascimento, data_atual.month, data_atual.day, 00, 00, 00)

    return start, end

def safe_lower(value):
    return value.lower() if isinstance(value, str) else ""

def listar_partidos():
    partidos = []
    for partido in partido_collection.find({}, {"_id": 0}):  # Projeta para excluir o campo _id
        partidos.append(partido)  # Adiciona cada partido à lista
    return partidos

def listar_cargos():
    cargos = politico_collection.distinct("cargo")
    cargos.insert(0,'Selecione o Cargo')
    return cargos

def listar_estados():
    estados = cidade_collection.distinct("estado")
    estados.insert(0,'Selecione o Estado')
    return estados

def listar_cidades(estado):
    cidades_filtradas = cidade_collection.find({"estado": estado})
    cidades = cidades_filtradas.distinct("nome")
    cidades.insert(0,'Selecione a cidade')
    return cidades

def listar_raca():
    racas = politico_collection.distinct("raca")
    racas.insert(0,'Selecione a Raça')
    return racas

def listar_genero():
    generos = politico_collection.distinct("genero")
    generos.insert(0,'Selecione o Gênero')
    return generos

def listar_ocupacao():
    ocupacoes = politico_collection.distinct("ocupacao")
    ocupacoes.insert(0,'Selecione a Ocupação')
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
