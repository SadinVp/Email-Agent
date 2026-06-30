from tools.emailTool import send_email
from tools.read_email_tool import read_emails

class EmailAgent:
    def run(self):
        print("Welcome to the Email Agent!")
        print("1. Send Email")
        print("2. Read Latest Emails")

        choice = input("\nChoose an option: ")
        if choice == "1":

            receiver = input("Enter the receiver's email address: ")
            subject =  input("Enter the subject of the email: ")
            body = input("Enter the body of the email: ")

            result = send_email(receiver, subject, body)

            if result["success"]:
                print("Email sent successfully!")
            else:
                print(f"Failed to send email: {result['error']}")
        elif choice == "2":
            result = read_emails()

            if result["success"]:

                print("\nLatest Emails\n")

                for mail in result["emails"]:

                    print(f"From    : {mail['from']}")
                    print(f"Subject : {mail['subject']}")
                    print("-" * 50)

            else:

                print(result["error"])
        
        else:
            print("Invalid choice. Please select either 1 or 2.")

