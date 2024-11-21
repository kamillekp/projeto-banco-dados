import tkinter as tk

def exibir_selecionados():
    # Exibe os itens selecionados
    selecionados = [opcoes[i] for i, var in enumerate(variaveis) if var.get() == 1]
    print("Selecionados:", ", ".join(selecionados))

# Inicializa a janela principal
root = tk.Tk()
root.title("Múltipla Escolha")

# Opções para múltipla escolha
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

# Lista de variáveis associadas aos checkboxes
variaveis = [tk.IntVar() for _ in opcoes]

# Cria os checkboxes
for i, opcao in enumerate(opcoes):
    tk.Checkbutton(root, text=opcao, variable=variaveis[i]).pack(anchor="n")

# Botão para exibir as escolhas selecionadas
tk.Button(root, text="Exibir Selecionados", command=exibir_selecionados).pack()

# Inicia o loop principal
root.mainloop()
