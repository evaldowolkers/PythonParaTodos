from carro1 import Carro1
from barco1 import Barco1

class Anfibio(Carro1, Barco1):
    def __init__(self, velocidade_em_terra, velocidade_na_agua,
                 qtd_portas, helices):
        self.velocidade_em_terra = velocidade_em_terra
        self.velocidade_na_agua = velocidade_na_agua
        self.qtd_portas = qtd_portas
        self.helices = helices

        super(Anfibio, self).__init__(velocidade_em_terra=velocidade_em_terra,
                                      velocidade_na_agua=velocidade_na_agua,
                                      qtd_portas=qtd_portas,
                                      helices=helices)

