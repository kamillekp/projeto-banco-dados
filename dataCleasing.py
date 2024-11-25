import pandas as pd
from unidecode import unidecode


'''com tudo em caixa baixa, campos nulos, vazios, em branco retirados, vamos retirar todos os acentos possiveis agora do arquivo consulta_cand_2024/consulta_cand_2024_BRASIL_limpo.csv, sem contas o header'''

# lendo o arquivo
df = pd.read_csv('consulta_cand_2024/consulta_cand_2024_BRASIL_limpo.csv', sep=';', encoding='latin1')

# retirando acentos
for col in df.columns:
    df[col] = df[col].apply(lambda x: unidecode(str(x)))

# salvando o arquivo
df.to_csv('consulta_cand_2024/consulta_cand_2024_BRASIL_limpo.csv', sep=';', encoding='latin1', index=False)
