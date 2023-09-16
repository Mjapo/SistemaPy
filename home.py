import tkinter as tk
import subprocess
import sys

# Função para abrir os diferentes recursos
def abrir_login():
    try:
        subprocess.Popen(['python', 'login.py'])
    except Exception as e:
        print("Erro ao abrir o Login:", e)

def abrir_cadastro():
    try:
        subprocess.Popen(['python', 'cadastro.py'])
    except Exception as e:
        print("Erro ao abrir o Cadastro:", e)

def abrir_sistema():
    try:
        subprocess.Popen(['python', 'sistema.py'])
    except Exception as e:
        print("Erro ao abrir o Sistema:", e)

def abrir_painel():
    try:
        subprocess.Popen(['python', 'painel.py'])
    except Exception as e:
        print("Erro ao abrir o Painel:", e)

# Função para fechar o software
def fechar_software():
    sys.exit(0)

# Cria uma janela principal para a página inicial (home)
root = tk.Tk()
root.title("Página Inicial")
root.geometry("800x400")  # Definir o tamanho da janela

# Cria um frame para os botões
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Cria botões para as opções
login_button = tk.Button(button_frame, text="Login", width=15, height=2, command=abrir_login)
cadastro_button = tk.Button(button_frame, text="Cadastro", width=15, height=2, command=abrir_cadastro)
sistema_button = tk.Button(button_frame, text="Sistema", width=15, height=2, command=abrir_sistema)
painel_button = tk.Button(button_frame, text="Painel", width=15, height=2, command=abrir_painel)

# Adicione um botão para fechar o software
fechar_button = tk.Button(button_frame, text="Fechar", width=15, height=2, command=fechar_software)

# Posiciona os botões lado a lado
login_button.grid(row=0, column=0, padx=10)
cadastro_button.grid(row=0, column=1, padx=10)
sistema_button.grid(row=0, column=2, padx=10)
painel_button.grid(row=0, column=3, padx=10)
fechar_button.grid(row=0, column=4, padx=10)  # Adicione o botão de fechar

# Inicia a interface gráfica
root.mainloop()
