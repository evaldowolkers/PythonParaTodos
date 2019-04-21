class Carro(object):
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        if valor<0:
            raise ValueError("O valor do carro não pode ser negativo.")
        else:
            self.valor = valor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Valor: R$ {self.valor:.2f}"

fusquinha = Carro("VW", "Fusca", 8500)
print(fusquinha)
fusquinha = Carro("VW", "Fusca", -1)
print(fusquinha)

