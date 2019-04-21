from googletrans import Translator

texto_pt = input("Escreva uma frase: ")
translator = Translator()
texto_en = translator.translate(texto_pt, src="pt", dest="en")
print("Texto original:", texto_pt)
print("Tradução:", texto_en.text)