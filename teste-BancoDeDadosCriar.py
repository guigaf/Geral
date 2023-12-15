import sqlite3

# Conectar ao banco de dados (se não existir, será criado automaticamente)
conexao = sqlite3.connect('banco_de_dados.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar tabela de usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        senha TEXT
    )
''')

# Exemplo de inserção de usuário
nome_usuario = 'exemplo_02'
senha_usuario = 'senha_02'
cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome_usuario, senha_usuario))

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()
