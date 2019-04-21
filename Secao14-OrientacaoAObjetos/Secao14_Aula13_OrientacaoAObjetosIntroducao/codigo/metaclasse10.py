class PessoaMeta(type):
    # Inicializando a classe com o método __init_
    def __init__(cls, name, bases, dict):
        print("PessoaMeta: __init__")
        # Chamando o método init da classe base (type)
        super().__init__(name, bases, dict)
        # Criando uma variável de nível de classe que é um
        # dicionário que mapeia os parâmetros do construtor para uma
        # instância que foi construída com esses parâmetros
        cls._instance_map = {}

    # Interceptando a chamada para o construtor da classe
    # para verificar se um objeto já foi instanciado com
    # os valores passados para o construtor.
    # Se existir, ele retorna a instância já existente
    def __call__(cls, first_name, last_name):
        print("PessoaMeta: __call__")
        # Criando uma tupla com o conjunto (nome, sobrenome)
        key = (first_name, last_name)

        # Verificando se o conjunto (nome, sobrenome) não existe em _instance_map
        if key not in cls._instance_map:
            # Se não existir, será criada uma variável new_instance
            # que vai receber uma nova instância da classe Pessoa.
            # Chamando o método __call__ da classe base
            new_instance = super().__call__(first_name, last_name)
            # Adicionando a nova instância ao dicionário que criamos
            # para armazenar as instâncias com base na chave (nome, sobrenome)
            cls._instance_map[key] = new_instance
        # Devolve a instância armazenada conforme a chave (nome, sobrenome)
        return cls._instance_map[key]

class Pessoa(metaclass=PessoaMeta):
    def __init__(self, first_name, last_name):
        print("Pessoa: __init__")
        self.first_name = first_name
        self.last_name = last_name

pessoa1 = Pessoa("Evaldo", "Wolkers")
pessoa2 = Pessoa("Evaldo", "Wolkers")
pessoa3 = Pessoa("Seu", "Madruga")

print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa1 is pessoa2)
print((pessoa3 is pessoa1) or (pessoa3 is pessoa2))