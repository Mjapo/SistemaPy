import sqlite3

def inserir_dados(setor, nome, idade):
    try:
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Dados (Setor, Nome, Idade) VALUES (?, ?, ?)
        ''', (setor, nome, idade))
        
        conn.commit()  # Salvar as alterações no banco de dados
        conn.close()   # Fechar a conexão com o banco de dados
        
        return True
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        return False
