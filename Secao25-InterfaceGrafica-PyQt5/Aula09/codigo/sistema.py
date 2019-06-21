# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistema.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Código adicionado
import cadastro_cliente
import cadastro_fornecedor
import database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Cadastro = QtWidgets.QMenu(self.menubar)
        self.menu_Cadastro.setObjectName("menu_Cadastro")
        self.menu_Opera_es = QtWidgets.QMenu(self.menubar)
        self.menu_Opera_es.setObjectName("menu_Opera_es")
        self.menu_Ajuda = QtWidgets.QMenu(self.menubar)
        self.menu_Ajuda.setObjectName("menu_Ajuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Cliente = QtWidgets.QAction(MainWindow)
        self.action_Cliente.setObjectName("action_Cliente")
        self.action_Fornecedor = QtWidgets.QAction(MainWindow)
        self.action_Fornecedor.setObjectName("action_Fornecedor")
        self.action_Produto = QtWidgets.QAction(MainWindow)
        self.action_Produto.setObjectName("action_Produto")
        self.action_Entrada = QtWidgets.QAction(MainWindow)
        self.action_Entrada.setObjectName("action_Entrada")
        self.action_Sa_da = QtWidgets.QAction(MainWindow)
        self.action_Sa_da.setObjectName("action_Sa_da")
        self.action_Sobre = QtWidgets.QAction(MainWindow)
        self.action_Sobre.setObjectName("action_Sobre")
        self.menu_Cadastro.addAction(self.action_Cliente)
        self.menu_Cadastro.addAction(self.action_Fornecedor)
        self.menu_Cadastro.addAction(self.action_Produto)
        self.menu_Opera_es.addAction(self.action_Entrada)
        self.menu_Opera_es.addAction(self.action_Sa_da)
        self.menu_Ajuda.addAction(self.action_Sobre)
        self.menubar.addAction(self.menu_Cadastro.menuAction())
        self.menubar.addAction(self.menu_Opera_es.menuAction())
        self.menubar.addAction(self.menu_Ajuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Código adicionado
        self.action_Cliente.triggered.connect(self.abrirCadastroCliente)
        self.action_Fornecedor.triggered.connect(self.abrirCadastroFornecedor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_Cadastro.setTitle(_translate("MainWindow", "&Cadastro"))
        self.menu_Opera_es.setTitle(_translate("MainWindow", "&Operações"))
        self.menu_Ajuda.setTitle(_translate("MainWindow", "&Ajuda"))
        self.action_Cliente.setText(_translate("MainWindow", "&Cliente"))
        self.action_Fornecedor.setText(_translate("MainWindow", "&Fornecedor"))
        self.action_Produto.setText(_translate("MainWindow", "&Produto"))
        self.action_Entrada.setText(_translate("MainWindow", "&Entrada de Produtos"))
        self.action_Sa_da.setText(_translate("MainWindow", "&Saída de Produtos"))
        self.action_Sobre.setText(_translate("MainWindow", "&Sobre"))

    # Código adicionado
    def abrirCadastroCliente(self):
        JanelaCadastroCliente = QtWidgets.QDialog()
        ui = cadastro_cliente.Ui_Form()
        ui.setupUi(JanelaCadastroCliente)
        # ui.buttonBox.accepted.connect(metodos_cliente.cadastrarCliente)
        JanelaCadastroCliente.show()
        JanelaCadastroCliente.exec_()

    # Código adicionado
    def abrirCadastroFornecedor(self):
        JanelaCadastroFornecedor = QtWidgets.QDialog()
        ui = cadastro_fornecedor.Ui_Form()
        ui.setupUi(JanelaCadastroFornecedor)
        # ui.buttonBox.accepted.connect(metodos_cliente.cadastrarCliente)
        JanelaCadastroFornecedor.show()
        JanelaCadastroFornecedor.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

