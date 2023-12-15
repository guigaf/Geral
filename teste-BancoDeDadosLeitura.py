import sqlite3
import pandas as pd

# Conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

# Criar um DataFrame a partir dos dados na tabela 'usuarios'
df = pd.read_sql_query('SELECT * FROM usuarios', conexao)

# Mostrar o DataFrame no console
print(df)

# Fechar a conexão
conexao.close()
