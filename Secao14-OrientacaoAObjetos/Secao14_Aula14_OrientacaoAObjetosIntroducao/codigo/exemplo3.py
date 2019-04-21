from abc import ABCMeta, abstractmethod

class Carro(metaclass=ABCMeta):
    @property
    @abstractmethod
    def valor(self):
        return "Retorno de valor"

    @abstractmethod
    def ligar(self):
        # Sem implementação
        pass

class fusca(Carro):
    @property
    def valor(self):
        return "Propriedade concreta."

    def ligar(self):
        print("Uhu, o fusca ligou!!!")

fusquinha = fusca()
fusquinha.ligar()
print(fusquinha.valor)