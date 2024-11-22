import tkinter as tk 

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

retangulo_width = 335
retangulo_height = 22
retangulo_x1 = 300
retangulo_y1 = 220
spacing = 40

def create_rectangle_with_triangle(canvas, x1, y1, x2, y2, triangle_size=5):
    canvas.create_rectangle(x1, y1, x2, y2, fill=cor_botoes_inputs, outline=cor_setas_bordas)
    
    triangle_coords = [
        (x2 - triangle_size - 5, y1 + (y2 - y1) / 2 - triangle_size / 2),  
        (x2 - 5, y1 + (y2 - y1) / 2 - triangle_size / 2),                
        (x2 - triangle_size / 2 - 5, y1 + (y2 - y1) / 2 + triangle_size / 2) 
    ]
    canvas.create_polygon(triangle_coords, fill=cor_setas_bordas, outline=cor_setas_bordas)

# INICIALIZAÇÃO DA TELA
root = tk.Tk()
root.title("Sistema para pesquisas políticas")
root.resizable(False, False)
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=cor_background)
canvas.pack()

# BACKGROUND TITULO 
canvas.create_rectangle(largura_retangulo, canvas_height + 5, 100, 0, fill=cor_background_meio, outline='') 

# TÍTULO
canvas.create_rectangle(largura_retangulo, 100, 100, 0, fill=cor_background_titulo, outline='')   
canvas.create_text(400, 50, text="POLÍTICA TRANSPARENTE", font=("Lexend Peta Light", 20), fill=cor_texto)

# TEXTO CENTRO
opcoes = ["Nome:", "Idade:", "Raça:", "Gênero:", "Ocupação:", "Estado:", "Partido:", "Coligação:"]
variaveis = [tk.IntVar() for _ in opcoes]

for i, opcao in enumerate(opcoes):
    canvas.create_text(170, 150 + i * 40, text=opcao, font=("Lexend Peta Light", 10), fill=cor_texto, anchor="w")

# INPUTS CENTRO
for i in range(2):
    tk.Entry(root, width=55).place(x=300, y=145 + i * 40)


for i in range(6):
    x1 = retangulo_x1
    y1 = retangulo_y1 + i * spacing
    x2 = x1 + retangulo_width
    y2 = y1 + retangulo_height
    create_rectangle_with_triangle(canvas, x1, y1, x2, y2)

root.mainloop()
