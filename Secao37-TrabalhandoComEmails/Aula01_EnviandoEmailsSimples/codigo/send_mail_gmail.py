import smtplib as smtp

class EnviarEmailGMail():
    def enviar_email(self, de, senha, para, assunto, mensagem):
        para = para.split(",")
        mensagem = f"Subject: {assunto}\n\n{mensagem}".encode('utf-8')
        try:
            with smtp.SMTP_SSL('smtp.gmail.com', 465) as s:
                s.login(de, senha)
                s.sendmail(de, para, mensagem)
            print("E-mail enviado!")
        except Exception as erro:
            print("Não foi possível enviar o e-mail. Erro:", erro)