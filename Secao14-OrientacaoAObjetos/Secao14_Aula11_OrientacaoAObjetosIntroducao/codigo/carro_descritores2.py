class DescritorValor(object):
    def __init__(self):
        self.valor = {}

    def __get__(self, instance, owner):
        return self.valor[instance]

    def __set__(self, instance, value):
        if value<0:
            raise ValueError("O valor do carro não "
                             "pode ser negativo.")
        else:
            self.valor[instance] = value

    def __delete__(self, instance):
        del self.valor[instance]

class Carro(object):
    valor = DescritorValor()
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, " \
               f"Valor: R$ {self.valor:.2f}"

fusquinha = Carro("VW", "Fusca", 8500)
gol = Carro("VW", "GOL", 20000)
print(gol)
print(fusquinha)
fusquinha2 = Carro("VW", "Fusca 2", 700)
print(fusquinha2)
print(gol)
print(fusquinha)
