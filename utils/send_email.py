import smtplib
from email.mime.text import MIMEText
from email.header import Header
from devops_backend.settings import EMAIL_FROM, EMAIL_HOST, EMAIL_PORT, EMAIL_TO, EMAIL_HOST_PASSWORD


def send_mail(message_text, image_url):
    SMTP_SERVER = EMAIL_HOST
    SSL_PORT = EMAIL_PORT
    USER_NAME = EMAIL_FROM
    message = MIMEText(message_text, _subtype='html', _charset='utf-8')
    subject = '镜像build成功' + image_url
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = EMAIL_FROM
    message['To'] = EMAIL_TO
    smtp = smtplib.SMTP(SMTP_SERVER, SSL_PORT)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(USER_NAME, EMAIL_HOST_PASSWORD)
    smtp.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())
    return EMAIL_TO

