import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select nome, telefone from contatos")
resultado = cursor.fetchall()
for linha in resultado:
    print("Nome: %s\nTelefone: %s" % (linha))
cursor.close()
conexao.close()
