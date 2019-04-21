from googletrans import Translator


translator = Translator(service_urls=[
  'translate.google.com',
  'translate.google.com.br',
])

print(translator.translate('veritas lux mea', src='la', dest='pt'))
