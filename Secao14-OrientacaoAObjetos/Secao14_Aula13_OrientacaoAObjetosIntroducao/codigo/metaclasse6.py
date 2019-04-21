# Para criar nossa metaclasse, vamos declarar a classe herdando da classe type
class MinhaMetaClasse(type):
    pass

# A metaclasse (MinhaMetaClasse) pode ser usada como se fosse type
MinhaClasse = MinhaMetaClasse('MinhaClasse', (), {})

minhaInstancia = MinhaClasse()
print(type(minhaInstancia))