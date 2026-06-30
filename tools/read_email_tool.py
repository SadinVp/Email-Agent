import imaplib
import email
from email.header import decode_header

from config import EMAIL, PASSWORD

def read_emails(limit=5):
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(EMAIL, PASSWORD)
        imap.select('inbox')
        status, messages = imap.search(None, 'ALL')
        mail_ids = messages[0].split()
        
        latest_ids = mail_ids[-limit:]

        emails = []
        for mail_id in reversed(latest_ids):
            status, msg_data = imap.fetch(mail_id, "(RFC822)")
            for response in msg_data:

                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # Decode Subject
                    subject, encoding = decode_header(msg["Subject"])[0]

                    if isinstance(subject, bytes):
                        subject = subject.decode(
                            encoding if encoding else "utf-8"
                        )

                    # Decode Sender
                    sender = msg.get("From")

                    emails.append({
                        "from": sender,
                        "subject": subject
                    })

        imap.logout()

        return {
            "success": True,
            "emails": emails
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
