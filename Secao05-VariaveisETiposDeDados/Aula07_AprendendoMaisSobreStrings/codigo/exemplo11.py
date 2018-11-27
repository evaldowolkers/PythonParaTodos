#email = "joao.silva@gmail.com"
email = "evaldowolkers@gmail.com"
indice_arroba = email.index("@")
indice_ponto = email.index(".")
provedor = email[indice_arroba+1:indice_ponto]
print("O nome do provedor é:", provedor)