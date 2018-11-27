email = "joao.silva@gmail.com"
usuario, dominio = email.split("@")
indice_ponto = dominio.index(".")
provedor = dominio[0:indice_ponto]
print("O usuário é:", usuario)
print("O domínio é:", dominio)