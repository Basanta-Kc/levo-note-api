from flask_mail import Message
from mail import mail


def send_email(email, subject, html):
    """
    Send an email using the Flask-Mail extension.

    The email is sent asynchronously using the Flask-Mail extension.
    Therefore, this function does not block the calling thread, and
    it should be safe to call from within any thread.

    :param email: The email address to send to
    :param subject: The subject line of the email
    :param html: The HTML body of the email
    """
    from app import app

    with app.app_context():
        msg = Message(
            subject=subject,
            sender=app.config["MAIL_USERNAME"],  
            recipients=[email],  
        )
        msg.html = html
        mail.send(msg)
