class Classe_simples(): # Quando vazios, as chaves são opcionais, class Classe_simples:
    pass

print(type(Classe_simples)) # Qual o tipo do objeto? => <class 'type'>

obj = Classe_simples() # obj é uma instância da classe simples
print(type(obj)) # <class '__main__.Classe_simples'>

print(type(obj) == Classe_simples) # True, obj é do tipo Classe_simples


