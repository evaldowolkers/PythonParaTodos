# Para criar nossa metaclasse, vamos declarar a classe herdando da classe type
class MinhaMetaClasse(type):
    pass

# Definindo a metaclasse na declaração da classe
class MinhaClasse(metaclass=MinhaMetaClasse):
    pass

minhaInstancia = MinhaClasse()
print(type(minhaInstancia))

