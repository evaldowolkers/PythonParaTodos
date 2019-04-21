from googletrans import Translator

texto_en = input("Write a sentence: ")
translator = Translator()
texto_pt = translator.translate(texto_en, src="en", dest="pt")
print("Original text:", texto_en)
print("Translation:", texto_pt.text)