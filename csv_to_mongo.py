import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)  
db = client["candidatos"] 
collection = db["candidatos_2024"]  

# Carregar o arquivo CSV
caminho_csv = "/consulta_cand_2024/consulta_cand_2024_BRASIL_limpo.csv"
df = pd.read_csv(caminho_csv)

# Converter os dados para um formato dicionário
dados = df.to_dict(orient="records")

# Inserir os dados no MongoDB
collection.insert_many(dados)

print(f"{len(dados)} documentos inseridos na coleção '{collection.name}' do banco de dados '{db.name}'.")
