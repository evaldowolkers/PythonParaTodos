import tempfile

print("Diretório temporário corrente:", tempfile.gettempdir())
# Vamos alterar o diretório temporário para C:\temp
# Para que seja reconhecida a contra-barra devemos colocar duas "\\"
tempfile.tempdir = "C:\\temp"
print("Diretório temporário após alteração:", tempfile.gettempdir())

# Veja agora onde nosso arquivo temporário será criado
with tempfile.TemporaryFile() as arq:
    print("Nome do arquivo:", arq.name)