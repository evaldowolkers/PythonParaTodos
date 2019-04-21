class Animal(object):
    def emitir_som(self):
        print("Um som qualquer")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")

def barulho(animal):
    animal.emitir_som()

cao = Cachorro()
barulho(cao)