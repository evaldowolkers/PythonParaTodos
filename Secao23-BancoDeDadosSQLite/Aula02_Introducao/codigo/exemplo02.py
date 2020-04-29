import sqlite3

dados = [("Maradona", "9805-5969"),
         ("Messi", "4856-0102"),
         ("Zico", "6959-3207")]
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany('''
        insert into contatos (nome, telefone)
        values(?, ?)
    ''', dados)
conexao.commit()
cursor.close()
conexao.close()