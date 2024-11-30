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
    # Inicializando a lista de resultados
    politicos_encontrados = []  
    
    # Percorrer todos os documentos no banco de dados
    for politico in politico_collection.find({}, {"_id": 0}):  # Removendo o _id dos resultados
        # Aplicando os filtros manualmente
        if nome and nome.lower() not in politico["nome"].lower():
            continue  # Ignorar se o nome não corresponder

        if idade:
            ano_nascimento = _calcular_ano_nascimento(idade)
            if not (ano_nascimento <= politico["nascimento"].year < ano_nascimento + 1):
                continue  # Ignorar se a idade não corresponder

        if raca and raca.lower() not in politico["raca"].lower():
            continue  # Ignorar se a raça não corresponder

        if genero and genero.lower() not in politico["genero"].lower():
            continue  # Ignorar se o gênero não corresponder

        if ocupacao and ocupacao.lower() not in politico["ocupacao"].lower():
            continue  # Ignorar se a ocupação não corresponder

        if candidatura and candidatura.lower() not in politico["cargo"].lower():
            continue  # Ignorar se o cargo não corresponder

        # Se todos os filtros forem atendidos, adicionar o documento completo à lista de resultados
        politicos_encontrados.append(politico)
    
    return politicos_encontrados

def _calcular_ano_nascimento(idade):
    ano_atual = datetime.now().year
    return ano_atual - idade


# Supondo que o banco de dados esteja configurado corretamente

# # Teste com nome
# resultados = consultar_candidatos(nome="nelson pernomian")
# print(resultados)  # Espera-se que retorne todos os dados de "Maria Silva"

# Teste com idade
resultados = consultar_candidatos(idade=39, genero="masculino")
print(resultados)  # Espera-se que retorne candidatos com idade aproximada de 39 anos

# # Teste com raça
# resultados = consultar_candidatos(raca="Negra")
# print(resultados)  # Espera-se que retorne candidatos com raça "Negra"

# # Teste com gênero
# resultados = consultar_candidatos(genero="Feminino")
# print(resultados)  # Espera-se que retorne todos os candidatos do gênero feminino

# # Teste com cargo
# resultados = consultar_candidatos(candidatura="Deputada")
# print(resultados)  # Espera-se que retorne candidatos com o cargo "Deputada"
