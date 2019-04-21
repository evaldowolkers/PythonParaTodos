class Animal(object):
    def emitir_som(self):
        print("Um som qualquer")

#class Animal(object):
#    def emitir_som(self):
#        pass

class Girafa(Animal):
    def comer(self):
        print("A girafa está comendo.")

def barulho(animal):
    animal.emitir_som()

girafinha = Girafa()
barulho(girafinha)