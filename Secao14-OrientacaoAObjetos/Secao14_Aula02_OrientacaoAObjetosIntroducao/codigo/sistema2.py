from heroi2 import Heroi

# Heroi(voa, possui_arma, lanca_teia, frase_comum)
homem_aranha = Heroi(False, False, True, "")
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)

he_man = Heroi(False, True, False, "Eu tenho a força!")
he_man.frase_comum = "Eu tenho a força"
he_man.falar()

homem_aranha.detalhar()
he_man.detalhar()