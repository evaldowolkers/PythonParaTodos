import smtplib as smtp

def enviar_email():
    de = "****@gmail.com" # Usuário do GMail para envio
    senha = '****' # Senha
    para = ["evaldowolkers@gmail.com"] # Destinatário
    mensagem = "Subject: Teste\n\nTeste de envio de e-mail com TLS"  # Mensagem a ser enviada

    try:
        with smtp.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(de, senha) # Efetuando login com o usuário e senha
            s.sendmail(de, para, mensagem) # Enviando e-mail
            s.close() # Fechando a conexão
        print("E-mail enviado!")
    except Exception as erro:
        print("Não foi possível enviar o e-mail. Erro:", erro)

if __name__ == '__main__':
    enviar_email()