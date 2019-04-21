from abc import ABCMeta, abstractmethod

class Carro(metaclass=ABCMeta):
    @abstractmethod
    def ligar(self):
        # Sem implementação
        pass

class fusca(Carro):
    def __init__(self):
        print("Vou implementar o ligar.")

    def ligar(self):
        print("Uhu, o fusca ligou!!!")

fusquinha = fusca()
fusquinha.ligar()
