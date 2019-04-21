class Porta(object):
    def fechar(self):
        print("A porta foi fechada!")

    def abrir(self):
        print("A porta foi aberta!")

class Janela(object):
    def fechar(self):
        print("A janela foi fechada!")

    def abrir(self):
        print("A janela foi aberta!")

def realizar_abertura(o_que_abrir):
    o_que_abrir.abrir()

def realizar_fechamento(o_que_fechar):
    o_que_fechar.fechar()

porta = Porta()
janela = Janela()

realizar_abertura(porta)
realizar_abertura(janela)
realizar_fechamento(porta)
realizar_fechamento(janela)