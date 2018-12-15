from googletrans import Translator
from googletrans.gtoken import TokenAcquirer

texto_en = input("Write a sentence: ")

translator = Translator()
acquirer = TokenAcquirer()
acquirer.do(texto_en)

texto_pt = translator.translate(texto_en, src="en", dest="pt")

print("Original text:", texto_en)
print("Translation:", texto_pt.text)