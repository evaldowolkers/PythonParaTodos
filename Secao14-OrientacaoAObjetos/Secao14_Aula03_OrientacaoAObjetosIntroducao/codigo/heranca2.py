# Criando a classe base
class Pai():
    def __init__(self):
        print('Construindo a classe Pai')

# Classe filha herda da classe pai
#class Filha(Pai):
#    def __init__(self):
#        Pai.__init__(self)  # Chamando o construtor da classe pai direto

# Criada classe mãe
class Mae():
    def __init__(self):
        print('Construindo a classe Mãe')

# Mudar a classe filha para herdar de Mae
#class Filha(Mae):
#    def __init__(self):
#        Pai.__init__(self)  # Chamando o construtor
                            # da classe pai direto. E agora?

# Em vez de fixar a clase Pai, melhor seria usar super() para definir
# que o método __init__ chamado é o da classe base.
class Filha(Pai):
    def __init__(self):
        super().__init__()  # Chamando o construtor da classe pai (de quem é herdeira)

filha = Filha()
print(type(filha))