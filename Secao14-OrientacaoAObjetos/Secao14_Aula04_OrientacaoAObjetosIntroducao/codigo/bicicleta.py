from veiculo import Veiculo

class Bicicleta(Veiculo):
    possui_guidao = True

    def __init__(self, qtd_rodas):
        super().__init__(False, 2)

    def empinar(self):
        print("A bicicleta empinou.")