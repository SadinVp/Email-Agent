from tools.emailTool import send_email

class EmailAgent:
    def run(self):
        print("Welcome to the Email Agent!")

        receiver = input("Enter the receiver's email address: ")
        subject =  input("Enter the subject of the email: ")
        body = input("Enter the body of the email: ")

        result = send_email(receiver, subject, body)

        if result["success"]:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email: {result['error']}")