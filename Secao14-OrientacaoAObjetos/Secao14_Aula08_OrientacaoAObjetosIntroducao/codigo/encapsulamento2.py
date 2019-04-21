class Carro(object):
    def __init__(self, fabricante):
        self.__fabricante = fabricante

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def get_fabricante(self):
        return self.__fabricante

carro = Carro("Toyota")
# Lista os atributos e métodos da classe
print(dir(carro))

# Forma correta de acessar o atributo privado__fabricante
print(carro.get_fabricante())

carro.set_fabricante("Fiat")
print(carro.get_fabricante())

# Forma incorreta de acessar o atributo privado__fabricante
print(carro._Carro__fabricante)
