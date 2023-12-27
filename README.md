# Email Sending Script

This script reads a CSV file containing email data and sends an email for each row. A progress animation is displayed in the console while each email is being sent.

## How to Run the Script

1. Ensure that you have Python installed on your machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
3. Run the script using the command `python main.py`.

## CSV File Structure

The CSV file should have the following columns:

- `Subject`: The subject of the email.
- `Body`: The body of the email.
- `Email`: The recipient's email address.

Here's an example of how your CSV file should look:

```csv
Subject,Body,Email
Hello,This is a test email.,test@example.com
