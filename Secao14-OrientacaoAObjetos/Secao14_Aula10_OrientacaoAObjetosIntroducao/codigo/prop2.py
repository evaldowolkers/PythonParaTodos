class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros_percorridos = metros
        self._tempo_gasto = segundos
        self._velocidade = self._metros_percorridos / self._tempo_gasto

    @property
    def velocidade(self):
        return f"A média de velocidade foi: {self._velocidade:.2f} metros por segundo."

a = Arrancada(10, 30)
print(a.velocidade)
# Velocidade é uma função, mas foi assinada para ser uma propriedade