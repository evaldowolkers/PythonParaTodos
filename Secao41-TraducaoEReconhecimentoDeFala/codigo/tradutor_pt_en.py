from googletrans import Translator
from googletrans.gtoken import TokenAcquirer

texto_pt = input("Escreva uma frase: ")

translator = Translator()
acquirer = TokenAcquirer()
acquirer.do(texto_pt)

texto_en = translator.translate(texto_pt, src="pt", dest="en")

print("Texto original:", texto_pt)
print("Tradução:", texto_en.text)