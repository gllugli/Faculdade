import sqlite3

# Conectar ao banco de dados (Criar o arquivo se não existir)
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# Criando a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        idade INTEGER
    )
""")

# Inserindo um cliente
cursor.execute("INSERT INTO clientes (nome, email, idade) VALUES (?, ?, ?)", ('Gabriel', 'gabriel@gmail.com', 18))

conexao.commit()
conexao.close()