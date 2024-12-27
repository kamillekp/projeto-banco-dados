import tkinter as tk
from tkinter import ttk
import customtkinter
import consulta_candidatos as cc

def mostrar_resultado(resultado_pesquisa):
    # Cria a janela principal
    root = tk.Tk()
    root.title("Resultado da Pesquisa")
    
    # Adiciona um espaçamento para cada linha
    for info in resultado_pesquisa:
        # Para cada linha de dados, criamos um Label com os dados concatenados
        label = tk.Label(root, text=str(info), pady=10)  # pady adiciona o espaço entre as linhas
        label.pack()

    # Inicia a interface gráfica
    root.mainloop()

# Exemplo de dados
resultado_pesquisa = [
    {'nome': 'jose carlos pedreiro', 'raca': 'branca', 'genero': 'masculino', 'nascimento': '27/12/1985', 'estado': 'mg', 'cidade': 'itanhandu', 'instrucao': 'ensino medio incompleto', 'cargo': 'vereador', 'ocupacao': 'motorista particular', 'partido': 'partido renovacao democratica', 'coligacao': None},
    {'nome': 'jose carlos pedreiro', 'raca': 'parda', 'genero': 'masculino', 'nascimento': '19/09/1968', 'estado': 'rj', 'cidade': 'sapucaia', 'instrucao': 'ensino fundamental incompleto', 'cargo': 'vereador', 'ocupacao': 'padeiro, confeiteiro e assemelhados', 'partido': 'partido liberal', 'coligacao': None}
]

mostrar_resultado(resultado_pesquisa)
