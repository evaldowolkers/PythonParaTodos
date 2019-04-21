from abc import ABCMeta, abstractmethod

class Carro(metaclass=ABCMeta):
    @abstractmethod
    def ligar(self):
        # Sem implementação
        pass

class kombi(Carro):
    def __init__(self):
        print("Não vou implementar o ligar.")

furgao = kombi()

"""
Deu erro porque kombi não tem o método ligar implementado
Traceback (most recent call last):
  File "...exemplo1.py", line 19, in <module>
    furgao = kombi()
TypeError: Can't instantiate abstract class kombi with abstract methods ligar
"""