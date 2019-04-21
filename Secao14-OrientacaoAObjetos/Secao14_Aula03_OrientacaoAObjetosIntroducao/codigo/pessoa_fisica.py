from pessoa import Pessoa

class Pessoa_Fisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__( nome, idade)
        self.cpf = cpf

