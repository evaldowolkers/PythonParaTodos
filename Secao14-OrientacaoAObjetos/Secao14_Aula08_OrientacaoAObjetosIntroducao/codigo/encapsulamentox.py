class Carro(object):
    marca = "Ford"
    __modelo = "Focus"
    
    def __init__(self, fabricante):
        self.__fabricante = fabricante

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def get_fabricante(self):
        return self.__fabricante

carro = Carro("Toyota")
print(carro.get_fabricante())
carro.set_fabricante("Fiat")
print(dir(carro))
print(carro.get_fabricante())
print(carro._Carro__fabricante)

# Atribuindo um valor ao atributo com __setattr__
carro.__setattr__("_Carro__fabricante", "Ford")
print(carro.get_fabricante())