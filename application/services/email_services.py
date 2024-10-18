from flask_mail import Message
from mail import mail

def send_email(email):
    """Send an email notification."""
    from app import app
    with app.app_context():
        msg = Message(
            subject='Hello from the other side!',
            sender='devbasanta@gmail.com',  # Ensure this matches MAIL_USERNAME
            recipients=[email]  # Replace with the actual recipient's email
        )
        msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
        mail.send(msg)
    