import tempfile

with tempfile.TemporaryFile(mode='w+t') as arq:
    arq.writelines(['Curso Python para Todos\n',
                    'Trabalhando com arquivos e diretórios temporários\n'])
    arq.seek(0)
    print(arq.read())