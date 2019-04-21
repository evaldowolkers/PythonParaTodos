from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, quantidade_rodas):
        Veiculo.__init__(self, True, quantidade_rodas)