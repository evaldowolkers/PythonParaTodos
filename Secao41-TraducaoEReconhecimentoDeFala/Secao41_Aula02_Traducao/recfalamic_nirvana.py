from googletrans import Translator
from googletrans.gtoken import TokenAcquirer
import speech_recognition as sr



musica = ['Come as you are as you were', 'As I want you to be', 'As a friend as a friend']
r = sr.Recognizer()
linha = 0

while linha < len(musica):
    print("Fale a letra:", musica[linha])
    with sr.Microphone() as source:
	    audio = r.listen(source)

    try:
        fala = r.recognize_google(audio)
    except:
        print('Vamos começar novamente.')

    if fala:
        if fala.lower() == musica[linha].lower():
            print("Você falou corretamente.")
            linha += 1
        else:
            print("Sua fala não está correta. Você disse:")
            print(fala.lower())
            print("Quando deveria ter dito:")
            print(musica[linha].lower())

    if linha == len(musica):
        print('Ótimo trabalho!!!')