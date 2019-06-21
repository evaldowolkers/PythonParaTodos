# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_fornecedor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Código adicionado
import database

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 379)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnNovo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnNovo.setObjectName("btnNovo")
        self.horizontalLayout_4.addWidget(self.btnNovo)
        self.btnAlterar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAlterar.setObjectName("btnAlterar")
        self.horizontalLayout_4.addWidget(self.btnAlterar)
        self.btnSalvar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSalvar.setObjectName("btnSalvar")
        self.horizontalLayout_4.addWidget(self.btnSalvar)
        self.btnCancelar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.edtNome = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtNome.setObjectName("edtNome")
        self.gridLayout.addWidget(self.edtNome, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.edtCelular = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtCelular.setObjectName("edtCelular")
        self.gridLayout.addWidget(self.edtCelular, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edtEndereco = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtEndereco.setObjectName("edtEndereco")
        self.gridLayout.addWidget(self.edtEndereco, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edtTelefone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtTelefone.setObjectName("edtTelefone")
        self.gridLayout.addWidget(self.edtTelefone, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 501, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.edtNome, self.edtTelefone)
        Form.setTabOrder(self.edtTelefone, self.edtCelular)
        Form.setTabOrder(self.edtCelular, self.edtEndereco)
        Form.setTabOrder(self.edtEndereco, self.btnNovo)
        Form.setTabOrder(self.btnNovo, self.btnAlterar)
        Form.setTabOrder(self.btnAlterar, self.btnSalvar)
        Form.setTabOrder(self.btnSalvar, self.btnCancelar)
        Form.setTabOrder(self.btnCancelar, self.tableView)

        # Código adicionado
        self.bancodados = database.DataBase()
        self.bancodados.conectar()
        self.btnNovo.clicked.connect(self.novoFornecedor)
        self.btnAlterar.clicked.connect(self.alterarFornecedor)
        self.btnSalvar.clicked.connect(self.salvarFornecedor)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tableView.clicked.connect(self.selecionarLinha)

        self.listarFornecedores()
        self.desabilitarCampos()
        self.selecionarLinha()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Fornecedores"))
        self.btnNovo.setText(_translate("Form", "Novo"))
        self.btnAlterar.setText(_translate("Form", "Alterar"))
        self.btnSalvar.setText(_translate("Form", "Salvar"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))
        self.label_3.setText(_translate("Form", "Celular"))
        self.label_2.setText(_translate("Form", "Telefone"))
        self.label_4.setText(_translate("Form", "Endereço"))
        self.label.setText(_translate("Form", "Nome"))

    # Código adicionado
    def desabilitarCampos(self):
        self.edtNome.setEnabled(False)
        self.edtTelefone.setEnabled(False)
        self.edtCelular.setEnabled(False)
        self.edtEndereco.setEnabled(False)
        self.btnSalvar.setEnabled(False)
        self.btnCancelar.setEnabled(False)
        self.btnNovo.setEnabled(True)
        self.btnAlterar.setEnabled(True)
        self.tableView.setEnabled(True)

    # Código adicionado
    def habilitarCampos(self):
        self.edtNome.setEnabled(True)
        self.edtTelefone.setEnabled(True)
        self.edtCelular.setEnabled(True)
        self.edtEndereco.setEnabled(True)
        self.btnSalvar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnNovo.setEnabled(False)
        self.btnAlterar.setEnabled(False)
        self.tableView.setEnabled(False)

    # Código adicionado
    def listarFornecedores(self):
        # self.bancodados.conectar()
        self.model = self.bancodados.listarFornecedores()
        self.tableView.setModel(self.model)
        # self.bancodados.desconectar()

    # Código adicionado
    def novoFornecedor(self):
        self.habilitarCampos()
        self.limparCampos()
        self.edtNome.setFocus()
        self.acao = "Novo"

    # Código adicionado
    def alterarFornecedor(self):
        self.habilitarCampos()
        self.acao = "Alterar"

    # Código adicionado
    def salvarFornecedor(self):
        if self.acao == "Novo":
            self.inserirFornecedor()
        else:
            self.atualizarFornecedor()

        self.listarFornecedores()
        self.limparCampos()
        self.desabilitarCampos()
        self.selecionarLinha()

    # Código adicionado
    def cancelar(self):
        self.desabilitarCampos()
        self.selecionarLinha()

    # Código adicionado
    def inserirFornecedor(self):
        fornecedor = {}
        fornecedor['nome'] = self.edtNome.text()
        fornecedor['telefone'] = self.edtTelefone.text()
        fornecedor['celular'] = self.edtCelular.text()
        fornecedor['endereco'] = self.edtEndereco.text()

        self.bancodados.inserirFornecedor(fornecedor)

    # Código adicionado
    def atualizarFornecedor(self):
        fornecedor = {}
        fornecedor['idfornecedores'] = self.idfornecedores
        fornecedor['nome'] = self.edtNome.text()
        fornecedor['telefone'] = self.edtTelefone.text()
        fornecedor['celular'] = self.edtCelular.text()
        fornecedor['endereco'] = self.edtEndereco.text()

        self.bancodados.alterarFornecedor(fornecedor)

    # Código adicionado
    def limparCampos(self):
        self.edtNome.clear()
        self.edtTelefone.clear()
        self.edtCelular.clear()
        self.edtEndereco.clear()

    def selecionarLinha(self):
        linha = 0
        rows = self.tableView.selectionModel().selectedIndexes()
        if (rows):
            linha = rows[0].row()

        self.idfornecedores= self.model.record(linha).value("idfornecedores")
        self.edtNome.setText(self.model.record(linha).value("nome"))
        self.edtTelefone.setText(self.model.record(linha).value("telefone"))
        self.edtCelular.setText(self.model.record(linha).value("celular"))
        self.edtEndereco.setText(self.model.record(linha).value("endereco"))