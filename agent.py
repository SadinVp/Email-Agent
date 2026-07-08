from reasoning.intent import detect_intent
from tools.registry import TOOLS


class EmailAgent:

    def run(self):

        while True:

            user_input = input("\nWhat would you like me to do?\n> ")

            result = detect_intent(user_input)

            intent = result["intent"]

            if intent == "send_email":
                
                tool = TOOLS[intent]
                arguments = self.collect_arguments(tool)

                response = tool.execute(*arguments)


                if response["success"]:
                    print("Email Sent Successfully!")

                else:
                    print(response["error"])

            elif intent == "read_email":

                tool = TOOLS[intent]
                arguments = self.collect_arguments(tool)

                response = tool.execute(*arguments)

                if response["success"]:

                    print()

                    for mail in response["emails"]:

                        print(f"From    : {mail['from']}")
                        print(f"Subject : {mail['subject']}")
                        print("-" * 50)

                else:

                    print(response["error"])

            elif intent == "exit":

                print("Goodbye!")
                break

            else:

                print("Sorry, I didn't understand.")
    
    def collect_arguments(self,tool):

        arguments = []
        for parameter in tool.parameters:
            value = input(f"{parameter}: ")
            arguments.append(value)
        
        return arguments

