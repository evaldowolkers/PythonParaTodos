# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistema.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cadastro_cliente import Ui_Dialog
import metodos_cliente

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuConfigura_o = QtWidgets.QMenu(self.menubar)
        self.menuConfigura_o.setObjectName("menuConfigura_o")
        self.menu_Sistema = QtWidgets.QMenu(self.menuConfigura_o)
        self.menu_Sistema.setObjectName("menu_Sistema")
        self.menu_Relat_rios = QtWidgets.QMenu(self.menubar)
        self.menu_Relat_rios.setObjectName("menu_Relat_rios")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Clientes = QtWidgets.QAction(MainWindow)
        self.action_Clientes.setObjectName("action_Clientes")
        self.actionUsu_rios = QtWidgets.QAction(MainWindow)
        self.actionUsu_rios.setObjectName("actionUsu_rios")
        self.actionPermiss_es = QtWidgets.QAction(MainWindow)
        self.actionPermiss_es.setObjectName("actionPermiss_es")
        self.action_Fornecedores = QtWidgets.QAction(MainWindow)
        self.action_Fornecedores.setObjectName("action_Fornecedores")
        self.action_Produtos = QtWidgets.QAction(MainWindow)
        self.action_Produtos.setObjectName("action_Produtos")
        self.action_Or_amentos = QtWidgets.QAction(MainWindow)
        self.action_Or_amentos.setObjectName("action_Or_amentos")
        self.action_Clientes_2 = QtWidgets.QAction(MainWindow)
        self.action_Clientes_2.setObjectName("action_Clientes_2")
        self.action_Fornecedores_2 = QtWidgets.QAction(MainWindow)
        self.action_Fornecedores_2.setObjectName("action_Fornecedores_2")
        self.action_Produtos_2 = QtWidgets.QAction(MainWindow)
        self.action_Produtos_2.setObjectName("action_Produtos_2")
        self.action_Or_amentos_2 = QtWidgets.QAction(MainWindow)
        self.action_Or_amentos_2.setObjectName("action_Or_amentos_2")
        self.action_Gerais = QtWidgets.QAction(MainWindow)
        self.action_Gerais.setObjectName("action_Gerais")
        self.action_Cores = QtWidgets.QAction(MainWindow)
        self.action_Cores.setObjectName("action_Cores")
        self.menuCadastro.addAction(self.action_Clientes)
        self.menuCadastro.addAction(self.action_Fornecedores)
        self.menuCadastro.addAction(self.action_Produtos)
        self.menuCadastro.addAction(self.action_Or_amentos)
        self.menu_Sistema.addAction(self.action_Gerais)
        self.menu_Sistema.addAction(self.action_Cores)
        self.menuConfigura_o.addAction(self.actionUsu_rios)
        self.menuConfigura_o.addAction(self.actionPermiss_es)
        self.menuConfigura_o.addAction(self.menu_Sistema.menuAction())
        self.menu_Relat_rios.addAction(self.action_Clientes_2)
        self.menu_Relat_rios.addAction(self.action_Fornecedores_2)
        self.menu_Relat_rios.addAction(self.action_Produtos_2)
        self.menu_Relat_rios.addAction(self.action_Or_amentos_2)
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuConfigura_o.menuAction())
        self.menubar.addAction(self.menu_Relat_rios.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action_Clientes.triggered.connect(self.abrirCadastroCliente)

    def abrirCadastroCliente(self):
        JanelaCadastroCliente = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(JanelaCadastroCliente)
        ui.buttonBox.accepted.connect(metodos_cliente.cadastrarCliente)
		ui.buttonBox.rejected.connect(JanelaCadastroCliente.reject)
        JanelaCadastroCliente.show()
        retorno = JanelaCadastroCliente.exec_()

        if retorno == QtWidgets.QDialog.Accepted:
            print("Você pressionou OK!!!")
        else:
            print("Você pressionou Cancelar")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro"))
        self.menuConfigura_o.setTitle(_translate("MainWindow", "&Configurações"))
        self.menu_Sistema.setTitle(_translate("MainWindow", "&Sistema"))
        self.menu_Relat_rios.setTitle(_translate("MainWindow", "&Relatórios"))
        self.action_Clientes.setText(_translate("MainWindow", "&Clientes"))
        self.actionUsu_rios.setText(_translate("MainWindow", "Usuários"))
        self.actionPermiss_es.setText(_translate("MainWindow", "Permissões"))
        self.action_Fornecedores.setText(_translate("MainWindow", "&Fornecedores"))
        self.action_Produtos.setText(_translate("MainWindow", "&Produtos"))
        self.action_Or_amentos.setText(_translate("MainWindow", "&Orçamentos"))
        self.action_Clientes_2.setText(_translate("MainWindow", "&Clientes"))
        self.action_Fornecedores_2.setText(_translate("MainWindow", "&Fornecedores"))
        self.action_Produtos_2.setText(_translate("MainWindow", "&Produtos"))
        self.action_Or_amentos_2.setText(_translate("MainWindow", "&Orçamentos"))
        self.action_Gerais.setText(_translate("MainWindow", "&Gerais"))
        self.action_Cores.setText(_translate("MainWindow", "&Cores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

