class Terrestre(object):
    """
    Classe de veículos terrestres
    """
    anda_na_terra = True
    def __init__(self, velocidade):
        self.velocidade_em_terra = velocidade

class Aquatico:
    """
    Classe de veículos aquáticos
    """
    anda_na_agua = True
    def __init__(self, velocidade):
        self.velocidade_na_agua = velocidade

class Carro(Terrestre):
    """
    Classe de carros
    """
    rodas = 4
    def __init__(self, velocidade, qtd_portas):
        self.qtd_portas = qtd_portas
        super().__init__(velocidade)

class Barco(Aquatico):
    """
    Classe de barcos
    """
    def __init__(self, velocidade, helices):
        self.helices = helices
        super().__init__(velocidade)

class Anfibio(Carro, Barco):
    """
    Classe de anfíbios
    """
    def __init__(self, velocidade_em_terra, velocidade_na_agua,
                 qtd_portas, helices):
        self.velocidade_em_terra = velocidade_em_terra
        self.velocidade_na_agua = velocidade_na_agua
        self.qtd_portas = qtd_portas
        self.helices = helices

        Carro.__init__(self, velocidade_em_terra, qtd_portas)
        Barco.__init__(self, velocidade_na_agua, helices)

meu_anfibio = Anfibio(100, 20, 4, 2)

print(meu_anfibio.velocidade_na_agua)
print(meu_anfibio.velocidade_em_terra)
print(meu_anfibio.qtd_portas)
print(meu_anfibio.helices)
print(meu_anfibio.anda_na_agua)
print(meu_anfibio.anda_na_terra)
print(meu_anfibio.rodas)
