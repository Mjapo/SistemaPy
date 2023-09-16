import sqlite3
import os

def inserir_dados(setor, nome, idade):
    try:
        # Obtém o diretório atual do script
        diretorio_atual = os.path.dirname(__file__)

        # Constrói o caminho para o banco de dados na mesma pasta do script
        caminho_banco = os.path.join(diretorio_atual, 'dados.db')

        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Dados (Setor, Nome, Idade) VALUES (?, ?, ?)
        ''', (setor, nome, idade))

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        return False
