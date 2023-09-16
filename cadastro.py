import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# Função para criar um hash da senha
def criar_hash_senha(senha):
    hash_obj = hashlib.sha256()
    hash_obj.update(senha.encode('utf-8'))
    return hash_obj.hexdigest()

# Função para realizar o cadastro
def cadastrar():
    # Obtém os dados do formulário
    email = email_entry.get()
    senha = senha_entry.get()

    # Conecta ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    try:
        # Verifica se o e-mail já existe no banco de dados
        cursor.execute("SELECT * FROM USUARIOS WHERE email=?", (email,))
        if cursor.fetchone() is not None:
            messagebox.showerror("Erro no cadastro", "Este e-mail já está cadastrado.")
        else:
            # Cria um hash da senha antes de armazená-la no banco de dados
            senha_criptografada = criar_hash_senha(senha)

            # Insere os dados na tabela USUARIOS
            cursor.execute("INSERT INTO USUARIOS (email, senha) VALUES (?, ?)",
                           (email, senha_criptografada))
            conn.commit()
            messagebox.showinfo("Cadastro bem-sucedido", "Cadastro realizado com sucesso!")
            limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro no cadastro", f"Ocorreu um erro ao cadastrar: {e}")
        conn.rollback()
    finally:
        conn.close()

# Função para limpar os campos do formulário
def limpar_campos():
    email_entry.delete(0, tk.END)
    senha_entry.delete(0, tk.END)

# Cria uma janela principal para a página de cadastro com tamanho personalizado
largura_janela = 500
altura_janela = 300
root = tk.Tk()
root.title("Cadastro")

# Centraliza a janela na tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Cria um frame para o formulário
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)  # Espaçamento interno usando padx e pady

# Rótulos e campos de entrada
email_label = tk.Label(frame, text="E-mail:")
email_entry = tk.Entry(frame)

senha_label = tk.Label(frame, text="Senha:")
senha_entry = tk.Entry(frame, show="*")  # A senha será exibida como asteriscos

# Botão para cadastrar
cadastrar_button = tk.Button(frame, text="Cadastrar", command=cadastrar)

# Posiciona os elementos na janela
email_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
email_entry.grid(row=0, column=1, padx=5, pady=5)

senha_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
senha_entry.grid(row=1, column=1, padx=5, pady=5)

cadastrar_button.grid(row=2, columnspan=2, pady=10)

# Inicia a interface gráfica
root.mainloop()

