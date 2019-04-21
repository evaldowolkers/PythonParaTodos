from abc import ABCMeta, abstractmethod

class Carro(metaclass=ABCMeta):
    @property
    @abstractmethod
    def valor(self):
        return "Retorno de valor"

    @abstractmethod
    def ligar(self):
        print("Método ligar da classe Carro")
        pass

class fusca(Carro):
    def ligar(self):
        print("Uhu, o fusca ligou!!!")

fusquinha = fusca()
fusquinha.ligar()
#print(fusquinha.valor)

