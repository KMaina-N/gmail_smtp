import smtplib, ssl
import json

def get_credentials_from_config():
    '''
    _summary_ 
        This function reads the config file and returns the email and password
    
    '''
    with open('config/config.json') as config_file:
        data = json.load(config_file)
    return data['EMAIL'], data['EMAIL_PASSWORD']


def send_email(subject, body, receiver_email):
    """_summary_
    Args:
        sender_email (_type_): _description_
        subject (_type_): _description_
        body (_type_): _description_
        receiver_email (_type_): _description_
    """
    port = 587 
    smtp_server = "smtp.gmail.com"
    sender_email, password = get_credentials_from_config()
    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        