class Heroi:
    """
    Classe de heróis
    """
    voa = False
    possui_arma = False
    lanca_teia = False
    frase_comum = ""
    
    def falar(self):
        print(self.frase_comum)

    def detalhar(self):
        if self.voa:
            print("O herói voa.")
        if self.possui_arma:
            print("O herói possui arma.")
        if self.lanca_teia:
            print("O herói lança teia.")