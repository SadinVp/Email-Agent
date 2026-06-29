from tools.emailTool import send_email

result = send_email(
    receiver="u2208047@rajagiri.edu.in",
    subject="Testing AI Agent",
    body="Hello! This is my first email tool."
)

print(result)