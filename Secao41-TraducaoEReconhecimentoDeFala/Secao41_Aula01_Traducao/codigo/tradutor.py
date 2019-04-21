from googletrans import Translator


translator = Translator()
# Se não for informada a linguagem de origem, o google translate tenta detectar a linguagem.
# A linguagem destino será inglês por padrão
print(translator.translate('안녕하세요.'))
# Aqui estamos definindo que a linguagem destino será Japonês
print(translator.translate('안녕하세요.', dest='ja'))
# Aqui estamos definindo a linguagem origem igual a Latin e a destino igual a Português
print(translator.translate('veritas lux mea', src='la', dest='pt'))