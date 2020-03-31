import tempfile

# Criando um arquivo temporário
arq = tempfile.TemporaryFile()

# Gravando informação no arquivo
arq.write(b'Curso Python para Todos')

# Indo para o início do arquivo
arq.seek(0)

# Imprimir o conteúdo do arquivo
print(arq.read())

# Fechar o arquivo
arq.close()