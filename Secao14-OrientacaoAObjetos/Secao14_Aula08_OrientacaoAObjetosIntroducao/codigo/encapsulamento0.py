class Carro(object):

    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

carro = Carro("Ford", "Ranger")
print(carro._marca)

# Não é correto acessar os atributos que iniciam com um
# underscore diretamente, o correto é usar os métodos get/set
carro._marca = "Fiat"
print(carro._marca)
carro.set_modelo("Uno")
print(carro.get_modelo())
print(carro.get_modelo())