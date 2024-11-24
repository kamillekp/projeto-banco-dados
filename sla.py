import tkinter as tk

def nova_tela():
    # Esconde o conteúdo atual
    label.pack_forget()
    button.pack_forget()

    # Cria novos widgets para a "nova tela"
    nova_label = tk.Label(root, text="Esta é a nova tela!")
    nova_label.pack()

    nova_button = tk.Button(root, text="Voltar", command=voltar)
    nova_button.pack()

def voltar():
    # Esconde os novos widgets
    nova_label.pack_forget()
    nova_button.pack_forget()

    # Volta para o conteúdo original
    label.pack()
    button.pack()

root = tk.Tk()

# Conteúdo inicial
label = tk.Label(root, text="Bem-vindo à tela inicial!")
label.pack()

button = tk.Button(root, text="Ir para a nova tela", command=nova_tela)
button.pack()

root.mainloop()
