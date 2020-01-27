import smtplib
import os

def send_email(user, pwd, recipient, subject, body):

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')


print('init send mail')

user = os.environ.get('MAIL_USERNAME')
pwd = os.environ.get('MAIL_PASSWORD')
recipient = os.environ.get('MAIL_RECIPIENT')

subject = 'asunto'
body = '<h1>Message titol</h1> \n\n\n this is the text message'

send_email(user, pwd, recipient, subject, body)

# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python