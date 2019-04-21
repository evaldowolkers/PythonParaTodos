from aquatico import Aquatico

class Barco(Aquatico):
    def __init__(self, velocidade_na_agua, helices):
        self.helices = helices
        super().__init__(velocidade_na_agua)