import smtplib

to = input("Enter the email of recipent : ")

content = input("Body : ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adithyahm7@gmail.com', 'gmailadi24')
    server.sendmail('adithyahm7@gmail.com', to, content)
    server.close()


sendEmail(to, content)
