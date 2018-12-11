from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,
                             QLabel, QWidget, QCheckBox, QRadioButton,
                             QProgressBar, QPushButton, QSlider)
from PyQt5.QtCore import Qt
import time

class ExemploAula4(QWidget):
    def __init__(self):
        super(ExemploAula4, self).__init__()
        self.setWindowTitle("PyQt5 Aula 4")
        self.setGeometry(200, 200, 200, 50)
        self.criar_grupo_checkbox()
        self.criar_grupo_radiobutton()
        self.criar_grupo_progressbar()
        self.criar_grupo_slider()
        self.definirLayoutTela()
        self.definirEventos()

    def criar_grupo_checkbox(self):
        self.label_checkbox = QLabel("Não Clicou")
        self.checkbox = QCheckBox("Olá, clique aqui.")
        layout_checkbox = QGridLayout()
        layout_checkbox.addWidget(self.checkbox, 0, 0)
        layout_checkbox.addWidget(self.label_checkbox, 1, 0, 1, 2)
        self.grupo_checkbox = QGroupBox("Caixa de Seleção")
        self.grupo_checkbox.setLayout(layout_checkbox)

    def criar_grupo_radiobutton(self):
        self.radiobutton1 = QRadioButton("Opção 1")
        self.radiobutton2 = QRadioButton("Opção 2")
        self.radiobutton3 = QRadioButton("Opção 3")
        self.radiobutton4 = QRadioButton("Opção 4")
        self.label_radiobutton = QLabel("Nenhuma opção selecionada.")
        layout_radiobutton = QGridLayout()
        layout_radiobutton.addWidget(self.radiobutton1, 0, 0)
        layout_radiobutton.addWidget(self.radiobutton2, 0, 1)
        layout_radiobutton.addWidget(self.radiobutton3, 1, 0)
        layout_radiobutton.addWidget(self.radiobutton4, 1, 1)
        layout_radiobutton.addWidget(self.label_radiobutton, 2, 0)
        self.grupo_radiobutton = QGroupBox("Botão de Rádio")
        self.grupo_radiobutton.setLayout(layout_radiobutton)

    def criar_grupo_progressbar(self):
        self.botao_progressbar = QPushButton("Animar barra progresso.")
        self.progressbar1 = QProgressBar()
        self.progressbar1.setMinimum(0)
        self.progressbar1.setMaximum(10)
        self.progressbar1.setOrientation(Qt.Horizontal)
        self.progressbar2 = QProgressBar()
        self.progressbar2.setMinimum(0)
        self.progressbar2.setMaximum(10)
        self.progressbar2.setOrientation(Qt.Vertical)
        layout_progressbar = QGridLayout()
        layout_progressbar.addWidget(self.progressbar1, 0, 0)
        layout_progressbar.addWidget(self.progressbar2, 0, 1)
        layout_progressbar.addWidget(self.botao_progressbar, 1, 0)
        self.grupo_progressbar = QGroupBox("Barra de Progresso")
        self.grupo_progressbar.setLayout(layout_progressbar)

    def criar_grupo_slider(self):
        self.slider = QSlider(Qt.Horizontal)
        #self.slider.setOrientation(Qt.Horizontal) #Pode ser usado das duas formas
        self.slider.setMaximum(20)
        self.label_slider = QLabel("Valor: 0")
        layout_slider = QGridLayout()
        layout_slider.addWidget(self.slider)
        layout_slider.addWidget(self.label_slider)
        self.grupo_slider = QGroupBox("Controle Deslizante")
        self.grupo_slider.setLayout(layout_slider)

    def definirEventos(self):
        # lambda -> Permite passar uma função como parâmetro, porque precisamos
        # passar o próprio checkbox/botão como parâmetro
        self.checkbox.stateChanged.connect(lambda:self.clicar_check_box(self.checkbox))
        self.radiobutton1.toggled.connect(lambda:self.clicar_radio_button(self.radiobutton1))
        self.radiobutton2.toggled.connect(lambda:self.clicar_radio_button(self.radiobutton2))
        self.radiobutton3.toggled.connect(lambda:self.clicar_radio_button(self.radiobutton3))
        self.radiobutton4.toggled.connect(lambda:self.clicar_radio_button(self.radiobutton4))
        self.botao_progressbar.clicked.connect(self.animar_progressbar)
        self.slider.valueChanged[int].connect(self.mover_slider)

    def clicar_check_box(self, cb):
        if cb.isChecked():
            self.label_checkbox.setText("Opção marcada")
        else:
            self.label_checkbox.setText("Opção desmarcada")

    def clicar_radio_button(self, rb):
        texto = "Opção Selecionada: " + rb.text()
        self.label_radiobutton.setText(texto)

    def animar_progressbar(self):
        for x in range(1, 11):
            self.progressbar1.setValue(x)
            self.progressbar2.setValue(x)
            time.sleep(1)

    def mover_slider(self, value):
        self.label_slider.setText("Valor: " + str(value))

    def definirLayoutTela(self):
        layoutTela = QGridLayout()
        layoutTela.addWidget(self.grupo_checkbox, 0, 0)
        layoutTela.addWidget(self.grupo_radiobutton, 0, 1)
        layoutTela.addWidget(self.grupo_progressbar, 1, 0)
        layoutTela.addWidget(self.grupo_slider, 1, 1)
        self.setLayout(layoutTela)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    janela = ExemploAula4()
    janela.show()
    sys.exit(app.exec_())