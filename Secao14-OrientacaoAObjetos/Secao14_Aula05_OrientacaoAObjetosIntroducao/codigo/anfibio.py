from carro import Carro
from barco import Barco

class Anfibio(Carro, Barco):
    def __init__(self, velocidade_em_terra, velocidade_na_agua,
                 qtd_portas, helices):
        self.velocidade_em_terra = velocidade_em_terra
        self.velocidade_na_agua = velocidade_na_agua
        self.qtd_portas = qtd_portas
        self.helices = helices

        Carro.__init__(self, velocidade_em_terra, qtd_portas)
        Barco.__init__(self, velocidade_na_agua, helices)

