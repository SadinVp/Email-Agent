from llm.client import analyze

decision = analyze(
    "Send an email to hr@company.com thanking them for the interview."
)

print(decision)