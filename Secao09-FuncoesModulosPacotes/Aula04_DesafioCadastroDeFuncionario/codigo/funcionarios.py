# Dicionário com código e nome do departamento
dados_departamento = {
    1: 'RH',
    2: 'FINANÇAS',
    3: 'SAC',
    4: 'VENDAS',
    5: 'TI'
}

# Dicionário contendo dicionários de funcionários, cada dicionário tem
# Nome, Data de admissão e Código do departamento
dados_funcionario = {
    100: dict(nome="José", admissao='01/05/2016', departamento=3),
    101: dict(nome="Maria", admissao='10/08/2018', departamento=1),
    102: dict(nome="Mariana", admissao='01/01/2019', departamento=4),
    103: dict(nome="Ana", admissao='18/05/2001', departamento=5),
    104: dict(nome="João", admissao='19/09/2014', departamento=1),
    105: dict(nome="Juca", admissao='25/07/2008', departamento=2)
}

# Método que recebe o código do funcionário por parâmetro e retorno o dicionário do funcionário
def get_funcionario(codigo):
    if codigo in dados_funcionario:
        return dados_funcionario[codigo]
    else:
        print("Funcionário de código", codigo, "não localizado.")
        return

# Método que percorre os itens do dicionário passado por parâmetro
# e imprime os campos nome, admissao e, em vez de imprimir o código do departamento,
# imprime o nome do departamento conforme o código que está no campo departamento
def imprimir_funcionario(funcionario):
    for chave, valor in funcionario.items():
        if chave == 'departamento':
            print(chave + ":", dados_departamento[valor])
        else:
            print(chave + ":", valor)

# Solicitando o código do funcionário
codigo = int(input("Informe o código do funcionário: "))
# Buscando o dicionário do funcionário de acordo com o código informado
funcionario = get_funcionario(codigo)

# Se encontrou o funcionário vai imprimir os dados, se não encontrou, a função get_funcionario já imprimiu
# informando que não foi localizado
if funcionario:
    imprimir_funcionario(funcionario)