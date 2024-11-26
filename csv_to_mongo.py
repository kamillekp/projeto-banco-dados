import pandas as pd
from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("URI")  #TODO: COLOCAR URL REMOTA
db = client["candidatos"]  # Nome do banco de dados
collection = db["candidatos_2024"]  # Nome da coleção

# Carregar o arquivo CSV
caminho_csv = "/consulta_cand_2024/consulta_cand_2024_BRASIL_limpo.csv"
df = pd.read_csv(caminho_csv)

dados = df.to_dict(orient="records")

# Inserir os dados no MongoDB
collection.insert_many(dados)

print(f"{len(dados)} documentos inseridos na coleção '{collection.name}' do banco de dados '{db.name}'.")
