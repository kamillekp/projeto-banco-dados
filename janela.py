import tkinter as tk 
from tkinter import ttk
import customtkinter
import consulta_candidatos as cc
import estatisticas_avancadas as ea
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

resultado_pesquisa = {}
pagina = 0
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
    global resultado_pesquisa
    resultado_pesquisa, query = cc.consultar_candidatos(nome, idade, raca, genero, ocupacao, candidatura, estado, cidade, partido)
    # Adicionando os resultados no frame com rolagem

    for widget in frame21.winfo_children():
        widget.destroy()

    for widget in frame22.winfo_children():
        widget.destroy()

    for widget in frame23.winfo_children():
        widget.destroy()

    for widget in frame24.winfo_children():
        widget.destroy()

    canvas_pagina.delete("texto")
    # LABELS COM INFORMAÇÕES
    global pagina                                                                         
    pagina = 0

    for j in range(pagina*50, (pagina+1)*50):

        if j>=len(resultado_pesquisa):
            break

        canvas_candidato = tk.Canvas(frame21, width=470, height=50, bg="white", borderwidth=0)
        canvas_candidato.pack()
        i = 10

        for chave, valor in resultado_pesquisa[j].items():
            if (chave=="partido"):
                partido_candidato = cc.get_partido(valor)
                canvas_candidato.create_text(350, 25, text=str(partido_candidato["sigla"]).upper(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
            else:
                canvas_candidato.create_text(i, 25, text=str(valor).title(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
                i+=250
    
    frame21.update_idletasks()
    
    pagina_texto = f'{pagina*50+1}-{(pagina+1)*50} de {len(resultado_pesquisa)}'
    if len(resultado_pesquisa)<(pagina+1)*50:
        pagina_texto = f'{pagina*50+1}-{len(resultado_pesquisa)} de {len(resultado_pesquisa)}'
         
    canvas_pagina.create_text(100,10, text=pagina_texto, 
                                font=("Lexend Peta Light", 9), 
                                fill=cor_texto, anchor="w", tag = "texto")

    # CRIAÇÃO DOS GRAFICOS DAS ESTATISTICAS
    if len(resultado_pesquisa) and not nome:

        fig = Figure(figsize = (2.3, 1.7), dpi = 100, facecolor=cor_background_meio) 
        fig2 = Figure(figsize = (2, 1.7), dpi = 100, facecolor=cor_background_meio) 
        fig3 = Figure(figsize = (1.9, 1.7), dpi = 100, facecolor=cor_background_meio) 

        frame21.configure(height = 250)
        frame21.place(relx=0.5, rely=0.25, anchor="center")
        canvas_pagina.place(relx=0.48, rely = 0.47)
        botao_esquerda.place(relx=0.85, rely = 0.47)
        botao_direita.place(relx=0.9, rely = 0.47)

        if (raca and not raca.startswith("Selecione")) and (genero and not genero.startswith("Selecione")): 
            frame23.place_forget()
            frame24.place_forget()

            frame22.configure(height = 250)
            frame22.place(relx=0.5, rely=0.7, anchor="center")
            
            fig = Figure(figsize = (3.5, 2.8), dpi = 100, facecolor=cor_background_meio) 

        elif raca and not raca.startswith("Selecione"): 
            frame24.place_forget()
            
            fig = Figure(figsize = (2.5, 2), dpi = 100, facecolor=cor_background_meio) 
            fig2 = Figure(figsize = (2.5, 2), dpi = 100, facecolor=cor_background_meio) 

            frame22.configure(height=160)
            frame22.place(relx=0.27, rely=0.7, anchor="center")
            
            frame23.configure(height=160)
            frame23.place(relx=0.73, rely=0.7, anchor="center")

        elif genero and not genero.startswith("Selecione"): 
            frame23.place_forget()

            fig = Figure(figsize = (2.5, 2), dpi = 100, facecolor=cor_background_meio) 
            fig3 = Figure(figsize = (2.5, 2), dpi = 100, facecolor=cor_background_meio) 

            frame22.configure(height=160)
            frame22.place(relx=0.27, rely=0.7, anchor="center")
            
            frame24.configure(height=160)
            frame24.place(relx=0.73, rely=0.7, anchor="center")
        
        else:
            frame21.configure(height = 200)
            frame21.place(relx=0.5, rely=0.2, anchor="center")
            canvas_pagina.place(relx=0.48, rely = 0.38)
            botao_esquerda.place(relx=0.85, rely = 0.38)
            botao_direita.place(relx=0.9, rely = 0.38)

            frame23.configure(height=130)
            frame23.place(relx=0.75, rely=0.53, anchor="center")

            frame24.configure(height=130)
            frame24.place(relx=0.5, rely=0.77, anchor="center")

            frame22.configure(height=130)
            frame22.place(relx=0.25, rely=0.53, anchor="center")


        # ESTATISTICAS DE NIVEL DE INSTRUÇÃO
        instrucao_estatisticas = ea.porcentagem_candidaturas_por_instrucao(query, len(resultado_pesquisa))

        plot1 = fig.add_subplot(111) 

        labels=[]
        for instrucao in instrucao_estatisticas.keys():
            labels.append(instrucao.replace(" ", "\n"))
            
        plot1.pie(instrucao_estatisticas.values(), 
                labels= labels, 
                autopct='%1.0f%%',
                labeldistance=1.2,
                textprops={'fontsize': 6},
                startangle=90)
    
        canvas = FigureCanvasTkAgg(fig, master = frame22)   
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.LEFT) 

        # ESTATISTICAS DE GENERO
        if not genero or genero.startswith("Selecione"):
            
            plot2 = fig2.add_subplot(111) 

            genero_estatisticas = ea.porcentagem_mulheres_candidatas(query, len(resultado_pesquisa))
            plot2.pie(genero_estatisticas.values(), 
                labels= genero_estatisticas.keys(), 
                autopct='%1.0f%%',
                textprops={'fontsize': 6},
                startangle=90
                )
            canvas2 = FigureCanvasTkAgg(fig2, master = frame23)   
            canvas2.draw() 
            canvas2.get_tk_widget().pack()
        
        # ESTATISTICAS DE RAÇA
        if not raca or raca.startswith("Selecione"):
            
            plot3 = fig3.add_subplot(111) 

            raca_estatisticas = ea.porcentagem_candidaturas_por_raca(query, opcoes_raca, len(resultado_pesquisa))
            plot3.pie(raca_estatisticas.values(), 
                labels= raca_estatisticas.keys(), 
                autopct='%1.0f%%',
                textprops={'fontsize': 6},
                startangle=90
                )
            canvas3 = FigureCanvasTkAgg(fig3, master = frame24)   
            canvas3.draw() 
            canvas3.get_tk_widget().pack()

    elif nome:
        frame22.place_forget()
        frame23.place_forget()
        frame24.place_forget()

        frame21.configure(height = 500)
        frame21.place(relx=0.5, rely=0.42, anchor="center")
        canvas_pagina.place(relx=0.48, rely = 0.85)
        botao_esquerda.place(relx=0.85, rely = 0.85)
        botao_direita.place(relx=0.9, rely = 0.85)

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

def listar_anteriores():
    global pagina
    if pagina:
        
        for widget in frame21.winfo_children():
            widget.destroy()

        pagina-=1
        for j in range(pagina*50, (pagina+1)*50):

            if j>=len(resultado_pesquisa):
                break

            canvas_candidato = tk.Canvas(frame21, width=470, height=50, bg="white", borderwidth=0)
            canvas_candidato.pack()
            i = 10

            for chave, valor in resultado_pesquisa[j].items():
                if (chave=="partido"):
                    partido_candidato = cc.get_partido(valor)
                    canvas_candidato.create_text(350, 25, text=str(partido_candidato["sigla"]).upper(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
                else:
                    canvas_candidato.create_text(i, 25, text=str(valor).title(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
                    i+=250
        
        frame21.update_idletasks()

        pagina_texto = f'{pagina*50+1}-{(pagina+1)*50} de {len(resultado_pesquisa)}'
        if len(resultado_pesquisa)<(pagina+1)*50:
            pagina_texto = f'{pagina*50+1}-{len(resultado_pesquisa)} de {len(resultado_pesquisa)}'
            
        canvas_pagina.delete("texto")
        canvas_pagina.create_text(100,10, text=pagina_texto, 
                                  font=("Lexend Peta Light", 9), 
                                  fill=cor_texto, anchor="w", tag = "texto")
        
def listar_posteriores():
    global pagina
    if (pagina+1)*50<=len(resultado_pesquisa):

        for widget in frame21.winfo_children():
            widget.destroy()

        pagina+=1
        for j in range(pagina*50, (pagina+1)*50):
            if j>=len(resultado_pesquisa):
                break

            canvas_candidato = tk.Canvas(frame21, width=470, height=50, bg="white", borderwidth=0)
            canvas_candidato.pack()
            i = 10

            for chave, valor in resultado_pesquisa[j].items():
                if (chave=="partido"):
                    partido_candidato = cc.get_partido(valor)
                    canvas_candidato.create_text(350, 25, text=str(partido_candidato["sigla"]).upper(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
                else:
                    canvas_candidato.create_text(i, 25, text=str(valor).title(), font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")
                    i+=250
        
        frame21.update_idletasks()

        pagina_texto = f'{pagina*50+1}-{(pagina+1)*50} de {len(resultado_pesquisa)}'
        if len(resultado_pesquisa)<(pagina+1)*50:
            pagina_texto = f'{pagina*50+1}-{len(resultado_pesquisa)} de {len(resultado_pesquisa)}'

        canvas_pagina.delete("texto")
        canvas_pagina.create_text(100,10, text=pagina_texto, 
                                  font=("Lexend Peta Light", 9), 
                                  fill=cor_texto, anchor="w", tag = "texto")

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
nomes_partidos = [partido['sigla'] for partido in opcoes_partidos]
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
frame21 = customtkinter.CTkScrollableFrame(principal_frame, width=500, height=200, fg_color="white")
frame21.place(relx=0.5, rely=0.2, anchor="center")

# FRAME PARA ESTATISTICAS
frame22 = tk.Frame(principal_frame, bg=cor_background_meio, width=550, height=130)
frame22.place(relx=0.25, rely=0.53, anchor="center")

frame23 = tk.Frame(principal_frame, bg=cor_background_meio, width=550, height=130)
frame23.place(relx=0.75, rely=0.53, anchor="center")

frame24 = tk.Frame(principal_frame, bg=cor_background_meio, width=550, height=130)
frame24.place(relx=0.5, rely=0.77, anchor="center")

# TEXTO DAS PAGINAS
canvas_pagina = tk.Canvas(principal_frame, width=200, height=20, bg=cor_background_meio)
canvas_pagina.place(relx=0.50, rely = 0.38)

# BOTÕES DAS PAGINAS DE LISTAGEM
botao_esquerda = tk.Button(principal_frame, text="<", font=("Lexend Peta Light", 7), bg=cor_background_meio, width=2, height=1, command=listar_anteriores) 
botao_esquerda.place(relx=0.85, rely = 0.38)

botao_direita = tk.Button(principal_frame, text=">", font=("Lexend Peta Light", 7), bg=cor_background_meio, width=2, height=1, command=listar_posteriores) 
botao_direita.place(relx=0.9, rely = 0.38)

# BOTÃO VOLTAR
tk.Button(principal_frame, text="Voltar", font=("Lexend Peta Light", 10), bg=cor_background_titulo, width=40, command=tela_principal).pack(pady=30, side=tk.BOTTOM)  # Posicionamento no final

#============================================================================================================================================
tela_principal()
root.mainloop()
