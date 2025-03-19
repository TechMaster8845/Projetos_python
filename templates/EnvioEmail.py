'''
Template
Útil para: Enviar notificações por e-mail automaticamente

'''
import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    remetente = "seuemail@gmail.com"
    senha = "sua_senha"

    msg = MIMEText(mensagem)
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

def main():
    enviar_email("destino@email.com", "Assunto do E-mail", "Olá, este é um teste!")

if __name__ == "__main__":
    main()
