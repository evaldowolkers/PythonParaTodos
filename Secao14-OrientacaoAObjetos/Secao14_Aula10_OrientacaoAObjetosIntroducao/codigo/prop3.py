class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros_percorridos = metros
        self._tempo_gasto = segundos
        self._velocidade = self._metros_percorridos / self._tempo_gasto

    def get_velocidade(self):
        print("Executou get_velocidade.")
        return f"A média de velocidade foi: {self._velocidade:.2f} metros por segundo."

    def set_velocidade(self, velocidade):
        print("Executou set_velocidade.")
        self._velocidade = velocidade

    def del_velocidade(self):
        print("Executou del_velocidade.")
        del self._velocidade

    velocidade = property(get_velocidade,
                          set_velocidade, del_velocidade,
                          "Propriedade velocidade do veículo.")

a = Arrancada(10, 30)
print(a.velocidade)
a.velocidade = 40
print(a.velocidade)
del a.velocidade
#Assinatura da função que cria a propriedade é:
#class property(fget=None, fset=None, fdel=None, doc=None)
#fget -> Função para obter um valor de atributo
#fset -> Função para definir um valor de atributo
#fdel -> Função para excluir um valor de atributo
#doc -> Cria uma docstring para o atributo