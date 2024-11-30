from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Conectar ao MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["candidatos"]

# Coleções
partido_collection = db["partidos"]
coligacao_collection = db["coligacoes"]
politico_collection = db["politicos"]

caminho_csv = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_acentos.csv"

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)

    #Partido
    partidos = df[["SG_PARTIDO", "NM_PARTIDO", "NR_PARTIDO"]].drop_duplicates()
    partido_ids = {}
    for _, row in partidos.iterrows():
        partido_doc = {
            "nome": row["NM_PARTIDO"],
            "numero": row["NR_PARTIDO"]
        }
        partido_id = partido_collection.insert_one(partido_doc).inserted_id
        partido_ids[row["SG_PARTIDO"]] = partido_id

    # Coligação
    coligacoes = df[["NM_COLIGACAO", "DS_COMPOSICAO_COLIGACAO"]].drop_duplicates()
    coligacao_ids = {}
    for _, row in coligacoes.iterrows():
        partidos_coligacao = [
            partido_ids[sg_partido.strip()] for sg_partido in row["DS_COMPOSICAO_COLIGACAO"].split("/") if sg_partido.strip() in partido_ids
        ]
        coligacao_doc = {
            "nome": row["NM_COLIGACAO"],
            "partidos": partidos_coligacao
        }
        coligacao_id = coligacao_collection.insert_one(coligacao_doc).inserted_id
        coligacao_ids[row["NM_COLIGACAO"]] = coligacao_id

    # Político
    for _, row in df.iterrows():
        politico_doc = {
            "nome": row["NM_URNA_CANDIDATO"],
            "raca": row["DS_COR_RACA"],
            "genero": row["DS_GENERO"],
            "nascimento": pd.to_datetime(row["DT_NASCIMENTO"], format='%d/%m/%Y', errors='coerce'),
            "ocupacao": row["DS_OCUPACAO"],
            "estado": row["SG_UF"],
            "cidade": row["NM_UE"],
            "instrucao": row["DS_GRAU_INSTRUCAO"],
            "cargo": row["DS_CARGO"],
            "partido": partido_ids.get(row["SG_PARTIDO"]),
            "coligacao": coligacao_ids.get(row["NM_COLIGACAO"])
        }
        politico_collection.insert_one(politico_doc)

    print("Dados processados e inseridos com sucesso!")
else:
    print(f"Arquivo não encontrado: {caminho_csv}")
