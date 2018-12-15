from googletrans import Translator


translator = Translator()
lista = ['Olá, tudo bem?', 'Bom dia', 'Eu tenho um cachorro.']
translations = translator.translate(lista, dest='fr')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)