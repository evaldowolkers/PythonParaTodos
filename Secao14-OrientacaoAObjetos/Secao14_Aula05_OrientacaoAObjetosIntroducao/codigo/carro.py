from terrestre import Terrestre

class Carro(Terrestre):
    rodas = 4
    def __init__(self, velocidade_em_terra, qtd_portas):
        self.qtd_portas = qtd_portas
        super().__init__(velocidade_em_terra)