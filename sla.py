import tkinter as tk
from tkinter import ttk

# Janela principal
root = tk.Tk()
root.title("Combobox com Estilo Personalizado")

# Estilo do Combobox
style = ttk.Style()

# Definindo o estilo para o Combobox
style.configure("TCombobox",
                fieldbackground="blue",  # Cor de fundo da área de entrada
                background="yellow",     # Cor de fundo da lista suspensa
                foreground="black",           # Cor do texto
                selectbackground="white",# Cor de fundo da seleção
                selectforeground="black",    # Cor do texto selecionado
                arrowcolor="red",             # Cor da seta
                relief="solid",               # Borda sólida
                borderwidth=2,                # Largura da borda
                width=40,                     # Largura do Combobox
                height=20)                    # Número de itens visíveis

# Lista de opções
options = [f"Opção {i}" for i in range(1, 21)]  # Exemplo de muitas opções

# Combobox com estilo personalizado
combobox = ttk.Combobox(root, values=options, state="normal", )
combobox.pack(pady=10)

# Executa a janela
root.mainloop()
