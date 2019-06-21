from PyQt5 import QtSql, QtCore
import mysql.connector

class DataBase():

    def conectar(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('127.0.0.1')
        self.db.setDatabaseName('cadastro')
        self.db.setUserName('root')
        self.db.setPassword('1234')
        if not self.db.open():
            print("Erro de conexão ao banco.")

    def desconectar(self):
        self.db.close()
        QtSql.QSqlDatabase.removeDatabase('QMYSQL')

    def listarClientes(self):
        model = QtSql.QSqlQueryModel()
        model.setQuery("select idclientes, nome, telefone, celular, endereco from clientes order by nome")
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Código")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Nome")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Telefone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Celular")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Endereco")
        return model

    def inserirCliente(self, cliente):
        query = QtSql.QSqlQuery()
        query.exec_(f"insert into clientes (nome, telefone, celular, endereco) values('{cliente['nome']}', '{cliente['telefone']}', '{cliente['celular']}', '{cliente['endereco']}')")

    def alterarCliente(self, cliente):
        query = QtSql.QSqlQuery()
        query.exec_(f"update clientes set nome='{cliente['nome']}', telefone='{cliente['telefone']}', celular='{cliente['celular']}', endereco='{cliente['endereco']}' where idclientes={cliente['idclientes']}")


    def listarFornecedores(self):
        model = QtSql.QSqlQueryModel()
        model.setQuery("select idfornecedores, nome, telefone, celular, endereco from fornecedores order by nome")
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Código")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Nome")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Telefone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Celular")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Endereco")
        return model

    def inserirFornecedor(self, fornecedor):
        query = QtSql.QSqlQuery()
        query.exec_(f"insert into fornecedores (nome, telefone, celular, endereco) values('{fornecedor['nome']}', '{fornecedor['telefone']}', '{fornecedor['celular']}', '{fornecedor['endereco']}')")

    def alterarFornecedor(self, fornecedor):
        query = QtSql.QSqlQuery()
        query.exec_(f"update fornecedores set nome='{fornecedor['nome']}', telefone='{fornecedor['telefone']}', celular='{fornecedor['celular']}', endereco='{fornecedor['endereco']}' where idfornecedores={fornecedor['idfornecedores']}")