class Documento(object):
    def __init__(self, nome):
        self.nome = nome

    def abrir(self):
        raise NotImplementedError("O método abrir deve ser implementado na subclasse.")

class Pdf(Documento):
    def abrir(self):
        return 'Foi aberto um arquivo PDF!'

class Doc(Documento):
    def abrir(self):
        return 'Foi aberto um arquivo DOC!'

class Xls(Documento):
    def abrir(self):
        return 'Foi aberto um arquivo DOC!'

documentos = [Pdf('Arquivo.pdf'),
              Pdf('Lista.pdf'),
              Doc('Documento.doc'),
              Xls('Planilha.xls')]

for documento in documentos:
    print(documento.abrir(), "de nome", documento.nome)

