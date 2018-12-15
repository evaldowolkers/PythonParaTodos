from googletrans import Translator


translator = Translator()
print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
print(translator.detect('この文章は日本語で書かれました。'))
print(translator.detect('This sentence is written in English.'))
print(translator.detect('Tiu frazo estas skribita en Esperanto.'))
print(translator.detect('Esta frase está escrita em Português'))
