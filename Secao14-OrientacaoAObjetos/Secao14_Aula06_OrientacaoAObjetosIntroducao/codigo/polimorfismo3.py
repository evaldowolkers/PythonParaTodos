class Animal(object):
    def emitir_som(self):
        raise NotImplementedError("Não foi implementado o método emitir_som.")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

class Girafa(Animal):
    def comer(self):
        print("A girafa está comendo.")

def barulho(animal):
    animal.emitir_som()

cachorrinho = Cachorro()
gatinho = Gato()
girafinha = Girafa()

barulho(cachorrinho)
barulho(gatinho)
barulho(girafinha)