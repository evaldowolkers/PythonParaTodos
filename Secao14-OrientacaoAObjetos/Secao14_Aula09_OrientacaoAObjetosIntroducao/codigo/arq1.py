class Arquivo1(object):
    def __init__(self):
        print("__name__:", __name__)

    def somar(self, x, y):
        return x + y

if __name__ == '__main__':
    a = Arquivo1()
    print("Soma em arq1:", a.somar(10 , 25))
