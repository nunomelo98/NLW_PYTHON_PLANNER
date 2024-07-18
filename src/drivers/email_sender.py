import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(to_addrs, body):
    from_addr = "email que foi criado com o create email"
    login = ""
    password = ""

    msg = MIMEMultipart()
    msg['From'] = "viagens_confirmar@email"
    msg["to"] = ', '.join(to_addrs)

    msg["subject"] = 'Confirmacao de Viagem !'

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.ethereal.email', 587)

    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit


