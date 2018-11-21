import send_mail_gmail as smg
import getpass

de = input("Informe seu usuário do GMail: ")
senha = getpass.getpass('Informe sua senha do GMail: ')
para = input('Informe o destinatário (ou vários separados por vírgula): ')
assunto = input("Informe o assunto/título do e-mail: ")
mensagem = input("Escreva a mensagem: ")

envio = smg.EnviarEmailGMail()
envio.enviar_email(de, senha, para, assunto, mensagem)
