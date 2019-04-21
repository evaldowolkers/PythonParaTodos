from classe_derivada1 import Classe_derivada1
from classe_derivada2 import Classe_derivada2

class Classe_teste():
    calculo = Classe_derivada1(10, 25)
    resultado = calculo.somar()
    print(resultado)
    resultado = calculo.subtrair()
    print(resultado)
    calculo.imprimir("Olá mundo!")

    calc = Classe_derivada2(70, 85)
    resultado = calc.multiplicar(20, 10)
    print(resultado)
    resultado = calc.somar()
    print(resultado)