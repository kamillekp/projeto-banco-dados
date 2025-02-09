from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import os
import re
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Conectar ao MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["candidatos"]

db.drop_collection("partidos")
db.drop_collection("coligacoes")
db.drop_collection("cidades")
db.drop_collection("politicos")

# Coleções
partido_collection = db["partidos"]
coligacao_collection = db["coligacoes"]
cidade_collection = db["cidades"]
politico_collection = db["politicos"]

caminho_csv = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_acentos.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
        
    # Cidade
    cidades = df[["SG_UF", "NM_UE"]].drop_duplicates()
    cidade_ids = {}
    for _, row in cidades.iterrows():
        cidade_doc = {
            "nome": row["NM_UE"],
            "estado": row["SG_UF"]
        }
        cidade_id = cidade_collection.insert_one(cidade_doc).inserted_id
        cidade_ids[row["NM_UE"]] = cidade_id

    # Partido
    partidos = df[["SG_PARTIDO", "NM_PARTIDO", "NR_PARTIDO"]].drop_duplicates()
    partido_ids = {}
    for _, row in partidos.iterrows():
        partido_doc = {
            "nome": row["NM_PARTIDO"],
            "sigla": row["SG_PARTIDO"],
            "numero": row["NR_PARTIDO"]
        }
        partido_id = partido_collection.insert_one(partido_doc).inserted_id
        partido_ids[row["SG_PARTIDO"]] = partido_id

    # Coligação
    coligacoes = df[["NM_UE", "NM_COLIGACAO", "DS_COMPOSICAO_COLIGACAO"]].drop_duplicates()
    coligacao_ids = {}
    for _, row in coligacoes.iterrows():
        if (row["DS_COMPOSICAO_COLIGACAO"] != 'partido isolado'):
            partidos_coligacao = [
                partido_ids[sg_partido.strip()] for sg_partido in re.split('/|\(|\)', row["DS_COMPOSICAO_COLIGACAO"]) if sg_partido.strip() in partido_ids
            ]
            coligacao_doc = {
                "nome": row["NM_COLIGACAO"],
                "cidade": row["NM_UE"], 
                "partidos": partidos_coligacao
            }
            if (row["NM_COLIGACAO"]!='partido isolado'):
                coligacao_id = coligacao_collection.insert_one(coligacao_doc).inserted_id
                coligacao_ids[row["NM_COLIGACAO"]] = coligacao_id

    # Político
    for _, row in df.iterrows():
        politico_doc = {
            "nome": row["NM_URNA_CANDIDATO"],
            "raca": row["DS_COR_RACA"],
            "genero": row["DS_GENERO"],
            "nascimento": pd.to_datetime(row["DT_NASCIMENTO"], format='%d/%m/%Y', errors='coerce'),
            "estado": row["SG_UF"],
            "cidade": row["NM_UE"],
            "instrucao": row["DS_GRAU_INSTRUCAO"],
            "cargo": row["DS_CARGO"],
            "ocupacao": row["DS_OCUPACAO"],
            "partido": partido_ids.get(row["SG_PARTIDO"]),
            "coligacao": coligacao_ids.get(row["NM_COLIGACAO"])
        }
        politico_collection.insert_one(politico_doc)

    print("Dados processados e inseridos com sucesso!")
else:
    print(f"Arquivo não encontrado: {caminho_csv}")
