import pandas as pd
from send_mail import send_email
import time
import threading

# Global flag to control the animation
email_sending = False

def progress():
    """
    This function does the following:
    Prints a progress animation to the console while an email is being sent.
    The animation runs in a separate thread and is controlled by the global
    'email_sending' flag.
    """
    # Print progress animation while the email is being sent
    while email_sending:
        print('#', end='', flush=True)
        time.sleep(0.1)

def send_emails_from_csv():
    '''
    This function does the following: 
        Reads a CSV file containing email data and sends an email for each row.
        The CSV file should have columns for 'Subject', 'Body', and 'Email'.
        A progress animation is displayed while each email is being sent.
    
    '''
    global email_sending
    # dataframe for the emails
    df = pd.read_csv('data/email.csv')

    for i in range(len(df)):
        # Start the progress animation
        email_sending = True
        t = threading.Thread(target=progress)
        t.start()

        # Send the email
        print(f"Sending email to {df['Email'][i]}")
        send_email(df['Subject'][i], df['Body'][i], df['Email'][i])

        # Stop the animation
        email_sending = False
        t.join()

        print("\nEmail sent")

if __name__ == "__main__":
    """
    Entry point for the script. Calls the 'send_emails_from_csv' function.
    """
    send_emails_from_csv()