import sqlite3
import os

if os.path.exists("agenda.db"):
    os.remove('agenda.db')

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute("""
                create table contatos(
                id integer primary key,
                nome varchar(100),
                telefone varchar(15))
                """)

cursor.execute("""
                insert into contatos (nome, telefone)
                values(?, ?)
                """, ('Evaldo', "1234-5678"))

conexao.commit()
cursor.close()
conexao.close()