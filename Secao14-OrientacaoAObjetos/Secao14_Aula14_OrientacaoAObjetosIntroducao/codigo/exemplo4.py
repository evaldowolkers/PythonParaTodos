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
    def ligar(self):
        print("Uhu, o fusca ligou!!!")

fusquinha = fusca()
fusquinha.ligar()
print(fusquinha.valor)

# Na hora de instanciar o objeto da classe fusca vai dar erro
# porque na classe fuscao não foi implementada a propriedade "valor"