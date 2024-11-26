'''Sabendo aue as regras do arquivo ./consulta_cand_2024/consulta_cand_2024_BRASIL.csv são:
- A codificação de caracteres dos arquivos é "Latin 1";
- Os campos estão entre aspas e separados por ponto e vírgula, inclusive os campos numéricos;
- Campos preenchidos com #NULO significam que a informação está em branco no banco de dados. O
correspondente para #NULO nos campos numéricos é -1;
- Campos preenchidos com #NE significam que naquele ano a informação não era registrada em banco de
dados pelos sistemas eleitorais. O correspondente para #NE nos campos numéricos é -3;
- O campo UF, além das unidades da federação, pode conter alguma das seguintes situações:
 o BR: quando se tratar de informação a nível nacional;
 o VT: quando se tratar de voto em trânsito;
 o ZZ: quando se tratar de Exterior.
- Os arquivos estão em constante processo de atualização e aperfeiçoamento. Alguns arquivos podem estar em
branco ou com mensagem de erro devido à indisponibilidade temporária na base de algum estado ou à
inexistência daquele arquivo para a época pretendida.
· -4, em caso de campos numéricos, exceto campo de idade;
· "NÃO DIVULGÁVEL", em caso de campos textuais;
· "", no caso de campos relativos a idade do candidato e sua data de nascimento.


exclua os dados nao divulgaveis, nulos, e NE e vazios 

alem disso, deixe apenas as seguintes colunas:
SG_UF - Sigla da unidade da federação na qual a candidata ou candidato concorre na eleição.
NM_UE Nome - da unidade eleitoral da candidata ou candidato. Em caso de abrangência nacional, é igual a "Brasil". Em caso de abrangência estadual, é o nome da UF em que a candidata ou candidato concorre. Em caso de abrangência municipal, é o nome do município em que a candidata ou candidato concorre.

NM_URNA_CANDIDATO  - Nome da candidata ou candidato que aparece na urna
NR_CANDIDATO - Número da candidata ou candidato na urna.

NM_CANDIDATO - Nome completo da candidata ou candidato.
DT_NASCIMENTO - Data de nascimento da candidata ou candidato.

DS_CARGO - Descrição do cargo ao qual a candidata ou candidato concorre.
DS_OCUPACAO - Descrição da ocupação da candidata ou candidato.

DS_GENERO -  Descrição do gênero da candidata ou candidato.

DS_GRAU_INSTRUCAO - Descrição do grau de instrução da candidata ou candidato

DS_COR_RACA - Descrição da cor/raça da candidata ou candidato.

NR_PARTIDO - Número do partido da candidata ou candidato.
SG_PARTIDO -  Sigla do partido da candidata ou candidato.
NM_PARTIDO - Nome do partido da candidata ou candidato.

NM_COLIGACAO - Nome da coligação pela qual o partido da candidata ou candidato concorre na eleição.
DS_COMPOSICAO_COLIGACAO -  Composição da coligação pela qual o partido da candidata ou candidato concorre na eleição. A informação da coligação é composta pela concatenação das siglas dos partidos coligados intercaladas com ','. Observação: quando o tipo de agremiação é por partido isolado ou federação a coluna DS_COMPOSICAO_COLIGACAO é preenchida, respectivamente, com a sigla do partido e a sigla da federação.
'''

import pandas as pd
import unidecode as unidecode

'''# Caminho para o arquivo CSV
file_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL.csv"

# Lendo o arquivo com codificação Latin 1 e separador ';'
df = pd.read_csv(file_path, encoding="latin1", sep=";")

# Selecionando as colunas desejadas
columns_to_keep = [
    "SG_UF", "NM_UE", "NM_URNA_CANDIDATO", "NR_CANDIDATO", "NM_CANDIDATO",
    "DT_NASCIMENTO", "DS_CARGO", "DS_OCUPACAO", "DS_GENERO", 
    "DS_GRAU_INSTRUCAO", "DS_COR_RACA", "NR_PARTIDO", "SG_PARTIDO", 
    "NM_PARTIDO", "NM_COLIGACAO", "DS_COMPOSICAO_COLIGACAO"
]
df = df[columns_to_keep]

# Removendo dados indesejados
invalid_values = ["#NULO", "#NE", "NÃO DIVULGÁVEL", "", -1, -3, -4]
df = df[~df.isin(invalid_values).any(axis=1)]  # Remove linhas com valores inválidos

# Convertendo todas as colunas de texto para caixa baixa
for column in df.columns:
    if df[column].dtype == "object":  # Apenas colunas de texto
        df[column] = df[column].str.lower()

# Salvando os dados processados em um novo arquivo
output_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado.csv"
df.to_csv(output_path, index=False, encoding="utf-8")'''


'''# agora, preciso que você crie um novo arquivo, a partir do ./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_interrogacao_contraria.csv e retire todos os acentos
# Lendo o arquivo processado
file_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_interrogacao_contraria.csv"
df = pd.read_csv(file_path)

# Removendo acentos
for column in df.columns:
    if df[column].dtype == "object":  # Apenas colunas de texto
        df[column] = df[column].fillna("").astype(str)  # Substitui NaN por string vazia e converte tudo para string
        df[column] = df[column].apply(unidecode.unidecode)  # Remove acentos

# Salvando os dados processados em um novo arquivo
output_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_acentos.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

# Exibindo as 5 primeiras linhas
pd.set_option('display.max_columns', None)  # Mostra todas as colunas ao printar
print(df.head())'''


'''# printar as 5 primeiras linhas do arquivo ./consulta_cand_2024/consulta_cand_2024_BRASIL.csv
file_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL.csv"
df = pd.read_csv(file_path, encoding="latin1", sep=";")

pd.set_option('display.max_columns', None)
print(df.iloc[4078:4083])'''

'''# Caminho do arquivo
file_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado.csv"
df = pd.read_csv(file_path)

# Substituir '?' dentro das strings de todas as colunas de texto
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].str.replace("¿", "", regex=False)

# Salvar o arquivo corrigido
output_path = "./consulta_cand_2024/consulta_cand_2024_BRASIL_processado_sem_interrogacao_contraria.csv"
df.to_csv(output_path, index=False, encoding="utf-8")'''