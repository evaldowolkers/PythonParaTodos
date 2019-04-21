from aquatico import Aquatico

class Barco1(Aquatico):
    def __init__(self, velocidade_na_agua, helices, **kwargs):
        self.helices = helices
        super().__init__(velocidade_na_agua)