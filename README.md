# Email Sending Script

This script reads a CSV file containing email data and sends an email for each row. A progress animation is displayed in the console while each email is being sent.

## How to Run the Script

1. Ensure that you have Python installed on your machine.
2. **Create a virtual environment:**
   - **Linux:**
     ```bash
     python3 -m venv env
     ```
   - **Windows:**
     ```bash
     python -m venv env
     ```
3. **Activate the virtual environment:**
   - **Linux:**
     ```bash
     source env/bin/activate
     ```
   - **Windows:**
     ```bash
     .\env\Scripts\activate
     ```
4. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

5. Run the script using the command `python main.py`.

## CSV File Structure

The CSV file should have the following columns:

- `Subject`: The subject of the email.
- `Body`: The body of the email.
- `Email`: The recipient's email address.

Here's an example of how your CSV file should look:

```csv
Subject,Body,Email
Hello,This is a test email.,test@example.com
