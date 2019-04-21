from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, qtd_rodas):
        super().__init__(True, qtd_rodas)