from flask_mail import Message
from mail import mail


def send_email(email, subject, html):
    """Send an email notification."""
    from app import app

    with app.app_context():
        msg = Message(
            subject=subject,
            sender="devbasanta@gmail.com",  # Ensure this matches MAIL_USERNAME
            recipients=[email],  # Replace with the actual recipient's email
        )
        msg.html = html
        mail.send(msg)
