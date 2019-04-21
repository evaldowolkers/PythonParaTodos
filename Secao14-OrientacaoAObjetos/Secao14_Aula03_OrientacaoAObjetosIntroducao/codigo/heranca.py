class Veiculo:
    """
    Classe de veículos
    """
    def __init__(self, possui_motor, quantidade_rodas):
        self.possui_motor = possui_motor
        self.quantidade_rodas = quantidade_rodas

    def ligar(self):
        if self.possui_motor:
            print("Ligou")
        else:
            print("Não tem motor.")

    def desligar(self):
        if self.possui_motor:
            print("Desligou")
        else:
            print("Não tem motor.")

    def andar(self):
        print("O veículo está andando.")

    def parar(self):
        print("O veículo foi parado.")

class Carro(Veiculo):
    """Classe carro herdando da classe Veiculo"""
    def __init__(self, quantidade_rodas):
        Veiculo.__init__(self, True, quantidade_rodas)

class Bicicleta(Veiculo):
    possui_guidao = True

    def __init__(self, quantidade_rodas):
        Veiculo.__init__(self, False, quantidade_rodas)

    def empinar(self):
        print("A bicicleta empinou.")

bike = Bicicleta(2)
print(bike.possui_guidao)
print(bike.quantidade_rodas)
bike.ligar()
bike.empinar()
bike.andar()
bike.parar()
bike.desligar()

carro = Carro(4)
print(carro.quantidade_rodas)
carro.ligar()
carro.andar()
carro.parar()
carro.desligar()