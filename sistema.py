import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para salvar os dados do formulário no banco de dados
def salvar_dados():
    # Obtém os dados dos campos de entrada
    internacao = internacao_entry.get()
    obito = obito_entry.get()
    alta = alta_entry.get()
    encaminhamento = encaminhamento_entry.get()
    transferencia = transferencia_entry.get()

    # Conecta ao banco de dados
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Insere os dados na tabela "USUARIOS" em vez da tabela "dados"
    cursor.execute("INSERT INTO USUARIOS (INTERNACAO, OBITO, ALTA, ENCAMINHAMENTO, TRANSFERENCIA_HOSPITALAR) VALUES (?, ?, ?, ?, ?)",
                   (internacao, obito, alta, encaminhamento, transferencia))

    # Salva as mudanças no banco de dados
    conn.commit()

    # Limpa os campos de entrada após a inserção
    internacao_entry.delete(0, tk.END)
    obito_entry.delete(0, tk.END)
    alta_entry.delete(0, tk.END)
    encaminhamento_entry.delete(0, tk.END)
    transferencia_entry.delete(0, tk.END)

    # Exibe uma mensagem de sucesso
    mensagem_sucesso = tk.Label(frame, text="Dados inseridos com sucesso!", fg="green")
    mensagem_sucesso.grid(column=0, row=6, columnspan=2)

# Cria uma janela principal
root = tk.Tk()
root.title("Formulário de Registro de Dados")

# Cria um frame para agrupar os elementos
frame = ttk.Frame(root, padding=50)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E))

# Cria rótulos e campos de entrada para cada tipo de dado
internacao_label = ttk.Label(frame, text="Internação:")
internacao_entry = ttk.Entry(frame)

obito_label = ttk.Label(frame, text="Óbito:")
obito_entry = ttk.Entry(frame)

alta_label = ttk.Label(frame, text="Alta:")
alta_entry = ttk.Entry(frame)

encaminhamento_label = ttk.Label(frame, text="Encaminhamento:")
encaminhamento_entry = ttk.Entry(frame)

transferencia_label = ttk.Label(frame, text="Transferência de Hospital:")
transferencia_entry = ttk.Entry(frame)

# Cria um botão para salvar os dados
salvar_button = ttk.Button(frame, text="Salvar", command=salvar_dados)

# Posiciona os elementos na janela usando o sistema de grid
internacao_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
internacao_entry.grid(column=1, row=0, padx=5, pady=5)

obito_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
obito_entry.grid(column=1, row=1, padx=5, pady=5)

alta_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
alta_entry.grid(column=1, row=2, padx=5, pady=5)

encaminhamento_label.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
encaminhamento_entry.grid(column=1, row=3, padx=5, pady=5)

transferencia_label.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)
transferencia_entry.grid(column=1, row=4, padx=5, pady=5)

salvar_button.grid(column=0, row=5, columnspan=2, pady=10)

# Inicia a interface gráfica
root.mainloop()
