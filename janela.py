import tkinter as tk 
from tkinter import ttk
import customtkinter
import consulta_candidatos as cc

resultado_pesquisa = []
#=============================================================================================================================================
def realizar_pesquisa():
    # Pegando os valores atuais dos campos de entrada
    nome = input1.get()
    idade = input2.get()
    raca = combobox1.get()
    genero = combobox2.get()
    ocupacao = combobox3.get()
    candidatura = combobox4.get()
    estado = combobox5.get()
    cidade = combobox6.get()
    partido = combobox7.get()

    # Chamando a função para consultar candidatos com os dados informados
    resultado_pesquisa = cc.consultar_candidatos(nome, idade, raca, genero, ocupacao, candidatura, estado, cidade, partido)

    # Adicionando os resultados no frame com rolagem
    for info in resultado_pesquisa:
        label = customtkinter.CTkLabel(frame21, text=info, font=("Arial", 5))
        label.pack(pady=10)

    # Exibindo o frame2 (onde os resultados são mostrados)
    tela_secundaria()

def seleciona_estado(evento):
    estado = evento.widget.get()
    opcoes_cidade = cc.listar_cidades(estado)
    combobox6.configure(values = opcoes_cidade, state='readonly')

def tela_principal():
    frame2.pack_forget()
    frame1.pack()

def tela_secundaria():
    frame1.pack_forget() 
    frame2.pack() 


#=============================================================================================================================================
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


#=============================================================================================================================================
# INICIALIZAÇÃO DA TELA---------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Sistema para pesquisas políticas")
root.resizable(False, False)
root.minsize(width=canvas_width, height=canvas_height)

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
opcoes_texto = ["Nome:", "Idade:", "Raça:", "Gênero:", "Ocupação:", "Candidatura:", "Estado:", "Cidade:", "Partido:"]
variaveis = [tk.IntVar() for _ in opcoes_texto]
for i, opcao in enumerate(opcoes_texto):
    canvas.create_text(170, 150 + i * 40, text=opcao, font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")

# INPUTS CENTRO (2 primeiros)
input1 = tk.Entry(frame1, width=55, bg=cor_botoes_inputs, highlightbackground=cor_setas_bordas, highlightthickness=0.2)
input1.place(x=300, y=145)
input2 = tk.Entry(frame1, width=55, bg=cor_botoes_inputs, highlightbackground=cor_setas_bordas, highlightthickness=0.2)
input2.place(x=300, y=185)

# COMBOBOXES CENTRO
opcoes_raca = cc.listar_raca()
opcoes_genero = cc.listar_genero()
opcoes_estados = cc.listar_estados()
opcoes_partidos = cc.listar_partidos()
opcoes_ocupacao = cc.listar_ocupacao()
opcoes_candidatura = cc.listar_cargos()
nomes_partidos = [partido['nome'] for partido in opcoes_partidos]
nomes_partidos.insert(0,'Selecione o Partido')

combobox1 = ttk.Combobox(frame1, values=opcoes_raca, state="readonly", height=10, width=52)
combobox1.place(x=300, y=220)
combobox2 = ttk.Combobox(frame1, values=opcoes_genero, state="readonly", height=10, width=52)
combobox2.place(x=300, y=260)
combobox3 = ttk.Combobox(frame1, values=opcoes_ocupacao, state="readonly", height=10, width=52)
combobox3.place(x=300, y=300)
combobox4 = ttk.Combobox(frame1, values=opcoes_candidatura, state="readonly", height=10, width=52)
combobox4.place(x=300, y=340)
combobox5 = ttk.Combobox(frame1, values=opcoes_estados, state="readonly", height=10, width=52)
combobox5.place(x=300, y=380)
combobox5.bind("<<ComboboxSelected>>", seleciona_estado)
combobox6 = ttk.Combobox(frame1, state="disabled", height=10, width=52)
combobox6.place(x=300, y=420)
combobox7 = ttk.Combobox(frame1, values=nomes_partidos, state="readonly", height=10, width=52)
combobox7.place(x=300, y=460)

# BOTÃO DE PESQUISA
pesquisa_botao = tk.Button(frame1, text="pesquisar", font=("Lexend Peta Light", 10), bg=cor_background_titulo, width=40, command=realizar_pesquisa)
pesquisa_botao.place(x=180, y=650)


#============================================================================================================================================
# FRAME SECUNDÁRIO ---------------------------------------------------------------------------------------------------------------------------
frame2 = tk.Frame(root, width=canvas_width, height=canvas_height , bg=cor_background)
frame2.pack(fill=tk.BOTH, expand=True)  
frame2.pack_propagate(False)

# TÍTULO
titulo_frame = tk.Frame(frame2, bg=cor_background_titulo, width=600, height=100)
titulo_frame.pack_propagate(False)
titulo_frame.pack()

titulo_label = tk.Label(titulo_frame, text="POLÍTICA TRANSPARENTE", font=("Lexend Peta Light", 20), fg=cor_texto, bg=cor_background_titulo)
titulo_label.pack(expand=True)

# FRAME CENTRAL
principal_frame = tk.Frame(frame2, bg=cor_background_meio, width=600, height=canvas_height+5)
principal_frame.pack_propagate(False)
principal_frame.pack()

# FRAME COM ROLAGEM
frame21 = customtkinter.CTkScrollableFrame(principal_frame, width=500, height=500, fg_color="white")
frame21.pack(side=tk.TOP)
frame21.place(relx=0.5, rely=0.45, anchor="center")

# LABELS COM INFORMAÇÕES                                                                          <------ PROBLEMA ESTÁ AQUI
for info in resultado_pesquisa:
    for chave, valor in info.items():
        label = tk.Label(frame21, text=f"{chave.capitalize()}: {valor}", pady=5)
        label.pack()

    label_espaco = tk.Label(frame21, text="", pady=10)
    label_espaco.pack()

frame21.update_idletasks() 

# BOTÃO VOLTAR
tk.Button(principal_frame, text="Voltar", font=("Lexend Peta Light", 10), bg=cor_background_titulo, width=40, command=tela_principal).pack(pady=30, side=tk.BOTTOM)  # Posicionamento no final


#============================================================================================================================================
tela_principal()
root.mainloop()
