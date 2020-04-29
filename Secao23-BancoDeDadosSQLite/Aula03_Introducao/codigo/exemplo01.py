import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
nome = input("Informe o nome do contato que quer apagar: ")
cursor.execute(f"delete from contatos where nome='{nome}'")
conexao.commit()
cursor.execute("select nome, telefone from contatos")
resultado = cursor.fetchall()
for linha in resultado:
    print("Nome: %s\nTelefone: %s" % (linha))
cursor.close()
conexao.close()
