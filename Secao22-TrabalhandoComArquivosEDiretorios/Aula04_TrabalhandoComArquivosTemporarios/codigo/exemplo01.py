import tempfile

# Criando um arquivo temporário
arq = tempfile.TemporaryFile()

# Imprimindo o objeto tempfile criado
print("Arquivo criado:", arq)

# Imprimindo o local e nome do arquivo temporário
print("Nome do arquivo:", arq.name)

# Fechando o arquivo
arq.close()