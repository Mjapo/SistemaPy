import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Correção na declaração SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    INTERNACAO TEXT,
    OBITO TEXT,
    ALTA TEXT,
    ENCAMINHAMENTO TEXT,
    TRANSFERENCIA_HOSPITALAR TEXT
);
""")

#conn.commit()
#conn.close()

print("conectado ao banco de dados")
