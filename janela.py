import tkinter as tk 
from tkinter import ttk
import requests

def tela_principal():
    frame2.pack_forget()
    frame1.pack()

def tela_secundaria():
    frame1.pack_forget() 
    frame2.pack() 


# CORES
cor_background = "#A7C5BD"
cor_background_meio = "#F7F0E1"
cor_background_titulo = "#FFCDA1"
cor_texto = "#2F2831"
cor_setas_bordas = "#C6C5C5"
cor_botoes_inputs = "#F3F3F3"
cor_opcoes = "#FFFFFF"

# TAMANHOS
canvas_width = 800
canvas_height = 720

largura_retangulo = 700

retangulo_width = 333
retangulo_height = 20
retangulo_x1 = 300
retangulo_y1 = 220
spacing = 40

# INICIALIZAÇÃO DA TELA---------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Sistema para pesquisas políticas")
root.resizable(False, False)


# FRAME PRINCIPAL---------------------------------------------------------------------------------------------------------------------------------------
frame1 = tk.Frame(root)
frame1.pack()

canvas = tk.Canvas(frame1, width=canvas_width, height=canvas_height, bg=cor_background)
canvas.pack()

# BACKGROUND PRINCIPAL----------------------------------------------------------------------------------------------------------------------------------
canvas.create_rectangle(largura_retangulo, canvas_height + 5, 100, 0, fill=cor_background_meio, outline='') 


# TÍTULO
canvas.create_rectangle(largura_retangulo, 100, 100, 0, fill=cor_background_titulo, outline='')   
canvas.create_text(400, 50, text="POLÍTICA TRANSPARENTE", font=("Lexend Peta Light", 20), fill=cor_texto)

# TEXTO CENTRO
opcoes_texto = ["Nome:", "Idade:", "Raça:", "Gênero:", "Ocupação:", "Estado:", "Partido:", "Coligação:"]
variaveis = [tk.IntVar() for _ in opcoes_texto]
for i, opcao in enumerate(opcoes_texto):
    canvas.create_text(170, 150 + i * 40, text=opcao, font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")

# INPUTS CENTRO (2 primeiros)
input1 = tk.Entry(frame1, width=55, bg=cor_botoes_inputs, highlightbackground=cor_setas_bordas, highlightthickness=0.2).place(x=300, y=145)
input2 = tk.Entry(frame1, width=55, bg=cor_botoes_inputs, highlightbackground=cor_setas_bordas, highlightthickness=0.2).place(x=300, y=185)


# COMBOBOXES CENTRO
opcoes_dropdown = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5", "Opção 6", "Opção 7", "Opção 8", "Opção 9", "Opção 10", "Opção 11", "Opção 12", "Opção 13", "Opção 14", "Opção 15", "Opção 16", "Opção 17", "Opção 18", "Opção 19", "Opção 20", "Opção 21", "Opção 22", "Opção 23", "Opção 24", "Opção 25", "Opção 26", "Opção 27", "Opção 28", "Opção 29", "Opção 30", "Opção 31", "Opção 32", "Opção 33", "Opção 34", "Opção 35", "Opção 36", "Opção 37", "Opção 38", "Opção 39", "Opção 40", "Opção 41", "Opção 42", "Opção 43", "Opção 44", "Opção 45", "Opção 46", "Opção 47", "Opção 48", "Opção 49", "Opção 50", "Opção 51", "Opção 52", "Opção 53", "Opção 54", "Opção 55", "Opção 56", "Opção 57", "Opção 58", "Opção 59", "Opção 60", "Opção 61", "Opção 62", "Opção 63", "Opção 64", "Opção 65", "Opção 66", "Opção 67", "Opção 68", "Opção 69", "Opção 70", "Opção 71", "Opção 72", "Opção 73", "Opção 74", "Opção 75", "Opção 76", "Opção 77", "Opção 78", "Opção 79", "Opção 80", "Opção 81", "Opção 82", "Opção 83", "Opção 84", "Opção 85", "Opção 86", "Opção 87", "Opção 88", "Opção 89", "Opção 90", "Opção 91", "Opção 92", "Opção 93"]
combobox1 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=220)
combobox2 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=260)
combobox3 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=300)
combobox4 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=340)
combobox5 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=380)
combobox6 = ttk.Combobox(frame1, values=opcoes_dropdown, state="readonly", height=10, width=52).place(x=300, y=420)


tk.Button(frame1, text="pesquisar", font=("Lexend Peta Light", 10), bg=cor_background_titulo, width=40, command=tela_secundaria).place(x=180, y=650)


# Frame 2
frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="Tela 2 com Canvas")
label2.pack(pady=10)

# Criando o Canvas no Frame 2
canvas = tk.Canvas(frame2, width=400, height=300)
canvas.pack()

# Criando um retângulo no Canvas
canvas.create_rectangle(50, 50, 350, 250, fill="blue", outline="black", width=2)

btn2 = tk.Button(frame2, text="Voltar para Tela 1", command=tela_principal)
btn2.pack(pady=5)

tela_principal()

root.mainloop()
