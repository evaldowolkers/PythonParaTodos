class Carro(object):
    marca = "Ford"
    __modelo = "Focus"

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

carro = Carro()
print(carro.marca)
carro.marca = "Fiat"
print(carro.marca)
carro.set_modelo("Uno")
print(carro.get_modelo())
carro._Carro__modelo = "Palio"
print(carro.get_modelo())