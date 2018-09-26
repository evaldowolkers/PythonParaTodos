"""
1) Crie um programa que possua duas variáveis denominadas nome e sobrenome.
Solicite que o usuário informe o nome e depois solicite que informe o sobrenome e grave nas variáveis separadamente.
Crie uma variável denominada nome_completo e grave o nome e sobrenome concatenados.
No final do programa imprima a frase:
Seu nome completo é: NOME SOBRENOME
Onde NOME e SOBRENOME é o conteúdo da variável nome_completo.
"""
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
nome_completo = nome + " " + sobrenome
print("Seu nome completo é:", nome_completo)