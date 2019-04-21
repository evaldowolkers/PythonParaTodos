class Cachorro(object):
    def som(self):
        print("au au")

class Gato(object):
    def som(self):
        print("Miau")

def emitir_som(animal):
    animal.som()

cachorrinho = Cachorro()
gatinho = Gato()

emitir_som(cachorrinho)
emitir_som(gatinho)