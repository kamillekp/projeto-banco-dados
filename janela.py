import tkinter as tk 
from tkinter import (font)

# CORES
cor_background = "#A7C5BD"
cor_background_meio = "#F7F0E1"
cor_background_titulo = "#FFCDA1"
cor_texto = "#2F2831"
cor_texto_inativo = "#A8A6A8"
cor_setas_bordas = "#C6C5C5"
cor_botoes_inputs = "#F3F3F3"
cor_opcoes = "#FFFFFF"

# TAMANHOS
canvas_width = 800
canvas_height = 720

largura_retangulo = 700


# INICIALIZAÇÃO DA TELA
root = tk.Tk()
root.title("Sistema para pesquisas políticas")
root.resizable(False, False)
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=cor_background)
canvas.pack()


# COMPONENTES DA TELA
canvas.create_rectangle(largura_retangulo, canvas_height + 5, 100, 0, fill=cor_background_meio, outline='')    # componente principal

# TÍTULO
canvas.create_rectangle(largura_retangulo, 100, 100, 0, fill=cor_background_titulo, outline='')   
canvas.create_text(400, 50, text="POLÍTICA TRANSPARENTE", font=("Lexend Peta Light", 20), fill=cor_texto)

# CENTRO
opcoes = ["Nome:", "Idade:", "Raça:", "Gênero:", "Ocupação:", "Estado:", "Partido:", "Coligação:"]
variaveis = [tk.IntVar() for _ in opcoes]

for i, opcao in enumerate(opcoes):
    canvas.create_text( 170, 150 + i * 40,  text=opcao,font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")

root.mainloop()