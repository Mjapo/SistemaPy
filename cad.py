import sqlite3
import hashlib

# Função para criar um hash da senha
def criar_hash_senha(senha):
    # Você pode escolher um algoritmo de hash, como SHA-256
    hash_obj = hashlib.sha256()
    hash_obj.update(senha.encode('utf-8'))
    return hash_obj.hexdigest()

# Conecta ao banco de dados
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

# Correção na declaração SQL da tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    senha TEXT
);
""")

# Exemplo de como inserir um usuário com senha criptografada
email = "usuario@example.com"
senha_plana = "senha123"  # Senha em texto plano
senha_criptografada = criar_hash_senha(senha_plana)

# Insere o usuário com a senha criptografada
cursor.execute("INSERT INTO USUARIOS (email, senha) VALUES (?, ?)",
               (email, senha_criptografada))

conn.commit()
conn.close()

print("Conectado ao banco de dados e inserido um usuário com senha criptografada")
