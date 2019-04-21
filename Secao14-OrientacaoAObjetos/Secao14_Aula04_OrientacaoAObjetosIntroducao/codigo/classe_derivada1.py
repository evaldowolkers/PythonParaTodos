from classe_base import Classe_base

class Classe_derivada1(Classe_base):
    def __init__(self, v1, v2):
        print("Método construtor da classe derivada1.")
        super().__init__(v1, v2)

    def imprimir(self, texto):
        print(texto)