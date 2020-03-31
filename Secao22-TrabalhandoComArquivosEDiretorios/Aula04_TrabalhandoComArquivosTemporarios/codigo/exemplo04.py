import tempfile

with tempfile.TemporaryFile() as arq:
    arq.write(b'Curso Python para Todos')
    arq.seek(0)
    print(arq.read())