import tempfile

with tempfile.TemporaryFile(prefix="Python_", suffix="_ParaTodos") as arq:
    print("Nome do arquivo:", arq.name)