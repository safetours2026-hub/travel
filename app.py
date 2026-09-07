from flask import Flask
import smtplib
from email.message import EmailMessage

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def hello_world():
    
    # 1. Configure email details
    SENDER_EMAIL = "safetours2026@gmail.com"
    SENDER_PASSWORD = "xgck vwaa ybnm tgyc"  # Do not use your regular login password
    RECIPIENT_EMAIL = "akhil.vviet@gmail.com"
    
    # 2. Build the email message
    msg = EmailMessage()
    msg['Subject'] = "Testing Python Email Automation"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content("Hello! This email was successfully sent using a Python script.")
    
    # 3. Connect to the SMTP server and send
    # Example below uses Gmail's secure port 465. Change server details for other hosts.
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        return 

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)
