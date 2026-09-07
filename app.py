from flask import Flask
import smtplib
from email.message import EmailMessage

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
    return Hello, World 

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)
