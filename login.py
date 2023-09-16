import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import os

# Função para verificar a senha no banco de dados
def verificar_senha(email, senha):
    # Conecta ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    try:
        # Consulta o banco de dados para verificar a senha
        cursor.execute("SELECT senha FROM USUARIOS WHERE email=?", (email,))
        resultado = cursor.fetchone()

        if resultado is not None:
            senha_armazenada = resultado[0]
            senha_criptografada = criar_hash_senha(senha)
            return senha_armazenada == senha_criptografada
        else:
            return False
    except Exception as e:
        messagebox.showerror("Erro de login", f"Ocorreu um erro ao fazer login: {e}")
        return False
    finally:
        conn.close()

# Função para criar um hash da senha
def criar_hash_senha(senha):
    hash_obj = hashlib.sha256()
    hash_obj.update(senha.encode('utf-8'))
    return hash_obj.hexdigest()

# Função para efetuar o login
def efetuar_login():
    email = email_entry.get()
    senha = senha_entry.get()

    if verificar_senha(email, senha):
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")
        abrir_pagina_home()
        limpar_campos()
    else:
        messagebox.showerror("Erro de login", "E-mail ou senha incorretos ou conta não cadastrada. Tente novamente.")

# Função para abrir a página "home"
def abrir_pagina_home():
    os.system("python home.py")  # Substitua "home.py" pelo nome do seu arquivo de página "home"

# Função para limpar os campos do formulário
def limpar_campos():
    email_entry.delete(0, tk.END)
    senha_entry.delete(0, tk.END)

# Cria uma janela principal para a página de login
root = tk.Tk()
root.title("Login")

# Cria um frame para o formulário
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Rótulos e campos de entrada
email_label = tk.Label(frame, text="E-mail:")
email_entry = tk.Entry(frame)

senha_label = tk.Label(frame, text="Senha:")
senha_entry = tk.Entry(frame, show="*")  # A senha será exibida como asteriscos

# Botão para efetuar o login
login_button = tk.Button(frame, text="Login", command=efetuar_login)

# Posiciona os elementos na janela
email_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
email_entry.grid(row=0, column=1, padx=5, pady=5)

senha_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
senha_entry.grid(row=1, column=1, padx=5, pady=5)

login_button.grid(row=2, columnspan=2, pady=10)

# Inicia a interface gráfica
root.mainloop()
