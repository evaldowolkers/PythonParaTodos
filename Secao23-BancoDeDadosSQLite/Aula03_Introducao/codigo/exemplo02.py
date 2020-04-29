import sqlite3


conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
nome = input("Informe o nome do contato que quer atualizar: ")
telefone = input(f"Informe o novo telefone do {nome}: ")
cursor.execute(f"update contatos set telefone={telefone} where nome='{nome}'")
conexao.commit()
cursor.execute("select nome, telefone from contatos")
resultado = cursor.fetchall()
for linha in resultado:
    print("Nome: %s\nTelefone: %s" % (linha))
cursor.close()
conexao.close()
