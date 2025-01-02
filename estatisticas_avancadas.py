from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import consulta_candidatos as cc
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")  # Banco de dados real
client = MongoClient(mongo_uri)
db = client["candidatos"]
politico_collection = db["politicos"]
partido_collection = db["partidos"]
coligacao_collection = db["coligacoes"]
cidade_collection = db["cidades"]

def porcentagem_candidaturas_por_instrucao(query, total:int):
    instrucoes_qtd = {}
    instrucoes_qtd['outros'] = 0

    query_instrucao = dict(query)

    for instrucao in politico_collection.distinct("instrucao"):
        query_instrucao['instrucao'] = instrucao
        qtd = politico_collection.count_documents(query_instrucao)
        if qtd/total <= 0.05:
            instrucoes_qtd["outros"] += qtd
        else:
            instrucoes_qtd[instrucao] = qtd

    if instrucoes_qtd['outros'] == 0:
        del instrucoes_qtd['outros']
        
    return instrucoes_qtd

def quantidade_candidaturas_por_partido(query, total:int):
    partidos_qtd = {}
    query_partido = dict(query)

    for partido in partido_collection.distinct("_id"):
        query_partido['partido'] = partido
        qtd = politico_collection.count_documents(query_partido)
        if qtd/total <= 0.05:
            partidos_qtd['outros'] += qtd
        else:
            partidos_qtd[cc.get_partido(partido)['sigla']] = qtd
       
    return partidos_qtd

def porcentagem_mulheres_candidatas(query: dict, total:int):
    generos_qtd = {}
    query_genero = dict(query)

    query_genero['genero'] = "masculino"
    generos_qtd["masculino"] = politico_collection.count_documents(query_genero)

    query_genero['genero'] = "feminino"
    generos_qtd["feminino"] = total - generos_qtd["masculino"]

    return generos_qtd

def porcentagem_candidaturas_por_raca(query: dict, opces_raca:list, total:int):
    racas_qtd = {}
    racas_qtd['outros'] = 0
    query_racas = dict(query)

    for raca in opces_raca:
        query_racas['raca'] = raca
        qtd = politico_collection.count_documents(query_racas)
        if qtd/total <= 0.05:
            racas_qtd['outros'] += qtd
        else:
            racas_qtd[raca] = qtd
    if racas_qtd['outros'] == 0:
        del racas_qtd['outros']
    return racas_qtd