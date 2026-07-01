from tools.base_tool import Tool
from tools.emailTool import send_email
from tools.read_email_tool import read_emails

TOOLS = {
    "send_email": Tool(
        name="send_email",
        description="Send an email to a recipient",
        parameters=[
            "receiver",
            "subject",
            "body"
        ],
        function=send_email
    ),
    "read_email": Tool(
        name="read_email",
        description="Read the latest emails",
        parameters=[],
        function=read_emails
    )

}