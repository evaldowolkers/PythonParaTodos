from heroi import Heroi

homem_aranha = Heroi()
homem_aranha.lanca_teia = True
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)

he_man = Heroi()
he_man.possui_arma = True
he_man.lanca_teia = False
he_man.voa = False
he_man.frase_comum = "Eu tenho a força"
he_man.falar()

homem_aranha.detalhar()
he_man.detalhar()