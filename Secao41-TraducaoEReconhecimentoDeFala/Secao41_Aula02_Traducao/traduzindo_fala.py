from googletrans import Translator
from googletrans.gtoken import TokenAcquirer
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
	print("Olá!!! Diga alguma coisa!!!")
	audio = r.listen(source)


texto = r.recognize_google(audio)
print("Texto: ", texto)

translator = Translator()
acquirer = TokenAcquirer()
acquirer.do(texto)
texto_ingles = translator.translate(texto, src="en", dest="pt")

print("Foi isso que você disse:\n", texto)
print("Tradução:\n", texto_ingles.text)