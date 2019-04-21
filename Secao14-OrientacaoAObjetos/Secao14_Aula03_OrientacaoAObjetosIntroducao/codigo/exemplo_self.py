class Quadrado():
    lados = 8
    def area(self): # self é uma referencia a uma instância
        return self.lados ** 2

quadrado = Quadrado()
print(quadrado.area()) # 64 ('lados' foi encontrado na classe)
print(Quadrado.area(quadrado)) # 64 (equivalente a quadrado.area())
                               # Aqui foi passada a instância para a chamada do método
quadrado.lados = 10
print(quadrado.area()) # 100 ('lados' foi encontrado na instância)

# Obs.: Podemos ter várias classes em um único arquivo
class Calculo():
    def calcular_total(self, quantidade, desconto):
        return (self.preco * quantidade - desconto)

calc = Calculo()
calc.preco = 15

print(calc.calcular_total(15, 10))
print(Calculo.calcular_total(calc, 15, 10))

