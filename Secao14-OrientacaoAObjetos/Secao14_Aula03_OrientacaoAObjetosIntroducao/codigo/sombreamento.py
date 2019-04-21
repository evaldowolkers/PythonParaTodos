class Ponto():
    x = 10
    y = 7

p = Ponto()

print(p.x) # 10 (do atributo da classe)
print(p.y) # 7 (do atributo da classe)
p.x = 12 # p obtém seu próprio atributo "x"
print(p.x) # 12 (encontrado na instância)
print(Ponto.x) # 10 (O atributo da classe ainda é o mesmo)
del p.x # Apagando o atributo da instância
print(p.x) # 10 (Agoa que não existe "x" na instância, será retornado da classe)
p.z = 3
print(p.z) # 3
print(Ponto.z) # O objeto Ponto não tem o atributo "z"
# AttributeError: type object 'Ponto' has no attribute 'z'