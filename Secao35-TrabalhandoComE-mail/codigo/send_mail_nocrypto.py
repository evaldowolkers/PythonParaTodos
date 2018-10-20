import smtplib as smtp

def enviar_email():
    de = "****@provedor.com.br" # Usuário da conta de e-mail de envio
    senha = '****' # Senha do usuário.
    para = ["****@provedor.com.br"] # Informe o(s) destino(s)
    mensagem = "Subject: Teste\n\nTeste de envio de e-mail" # Mensagem a ser enviada

    try:
        with smtp.SMTP('mail.topcard.com.br', 587) as s:
            s.login(de, senha) # Efetuando login com o usuário e senha
            s.sendmail(de, para, mensagem) # Enviando e-mail
            s.close() # Fechando a conexão
        print("E-mail enviado!")
    except Exception as erro:
        print("Não foi possível enviar o e-mail. Erro:", erro)

if __name__ == '__main__':
    enviar_email()