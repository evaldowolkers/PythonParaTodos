class Classe_base():
    def __init__(self, valor1, valor2):
        print("Método construtor da classe base")
        self.valor1 = valor1
        self.valor2 = valor2

    def somar(self):
        return self.valor1 + self.valor2

    def subtrair(self):
        return self.valor1 - self.valor2
