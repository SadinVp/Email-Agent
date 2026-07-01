from tools.emailTool import send_email
from tools.read_email_tool import read_emails

TOOLS = {
    "send_email": {
        "description": "Send an email to a recipient",
        "function": send_email
    },
    "read_email": {
        "description": "Read the latest emails",
        "function": read_emails
    }
}