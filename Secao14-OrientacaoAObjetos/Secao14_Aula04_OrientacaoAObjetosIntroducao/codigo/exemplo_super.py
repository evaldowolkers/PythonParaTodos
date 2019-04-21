class Pai():
    def __init__(self):
        print("Construtor da classe Pai")

class Mae():
    def __init__(self):
        print("Construtor da classe Mãe")

class Filha(Pai):
    def __init__(self):
        super().__init__()

filha = Filha()