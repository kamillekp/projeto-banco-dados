import tkinter as tk
import requests

def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            data = response.json()
            label_result["text"] = f"Título: {data['title']}"
        else:
            label_result["text"] = "Erro ao buscar dados"
    except Exception as e:
        label_result["text"] = f"Erro: {str(e)}"

# Interface Tkinter
root = tk.Tk()
root.title("Consumindo API")

btn_fetch = tk.Button(root, text="Buscar Dados", command=fetch_data)
btn_fetch.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
