import smtplib, ssl


def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'mithun.selvaraj@gmail.com'
    password = "zqesvsoospymkvbm"
    context = ssl.create_default_context()
    receiver = "mithun.selvaraj@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
