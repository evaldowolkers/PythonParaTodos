from veiculo import Veiculo

class Bicicleta(Veiculo):
    possui_guidao = True

    def __init__(self, quantidade_rodas):
        Veiculo.__init__(self, False, quantidade_rodas)

    def empinar(self):
        print("A bicicleta empinou.")