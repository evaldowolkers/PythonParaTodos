import tempfile

with tempfile.TemporaryDirectory() as tmpdirname:
    print('Diretório temporário:', tmpdirname)

# O diretório e seu conteúdo foi deletado