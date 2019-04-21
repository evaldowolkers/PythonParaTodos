from pessoa_fisica import Pessoa_Fisica
from pessoa_juridica import Pessoa_Juridica

pf = Pessoa_Fisica("012.345.678-90", "Evaldo", 38)
pj = Pessoa_Juridica("01.000.123/0001-00", "Loja Teste", 5)

print(pf.nome)
print(pf.cpf)
print(pj.nome)
print(pj.cnpj)