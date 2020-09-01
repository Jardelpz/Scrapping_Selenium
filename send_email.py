import smtplib
import os


from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import date
from socket import gethostname
from settings import EMAIL, EMAIL_PASSWORD

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(EMAIL, EMAIL_PASSWORD)


def send_email():
    os.getcwd()
    current_dir = r"C:\Users\jarde\Documents\webScrapping\Scrapping_Selenium\docs"
    bankslip_path = current_dir + '/boletos/boleto{}.pdf'.format(str(date.today()))
    image_path = current_dir + '/images/payment{}.png'.format(str(date.today()))
    try:
        message = f"Olá, Este email foi enviado pelo HOST: {gethostname()}. \n " \
                  f"Segue abaixo seu boleto do mês atual bem como seu histórico de pagamentos"
        msg = MIMEMultipart()
        msg['Subject'] = 'Boleto FURB'
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg.attach(MIMEText(message))

        with open(image_path, 'rb') as img:
            img_attach = MIMEImage(img.read(), _subtype="png")
            img_attach.add_header('Content-Disposition', 'attachment', filename="payments.png")
        msg.attach(img_attach)

        with open(bankslip_path, 'rb') as file:
            bankslip_attach = MIMEApplication(file.read(), _subtype="pdf")
            bankslip_attach.add_header('Content-Disposition', 'attachment',
                                       filename="Boleto do mês {}".format(date.today().month))
        msg.attach(bankslip_attach)
        smtpObj.send_message(msg)

    except:
        print("Error sending email")


send_email()
