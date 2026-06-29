import smtplib
from email.message import EmailMessage

from config import EMAIL, PASSWORD

def send_email(receiver, subject, body):

    message = EmailMessage()

    message["From"] = EMAIL
    message["To"] = receiver
    message["Subject"] = subject

    message.set_content(body)

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, PASSWORD)

            smtp.send_message(message)

        return {
            "success": True,
            "message": "Email sent successfully."
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }