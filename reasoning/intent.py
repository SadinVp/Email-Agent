# reasoning/intent.py

def detect_intent(user_input: str):
    """
    Detect what the user wants to do.
    This is currently rule-based.
    Later, an LLM will replace this function.
    """

    text = user_input.lower().strip()

    send_keywords = [
        "send",
        "compose"
    ]

    read_keywords = [
        "read",
        "show",
        "inbox",
        "latest"
    ]

    exit_keywords = [
        "exit",
        "quit",
        "bye"
    ]

    if any(word in text for word in send_keywords):
        return {
            "intent": "send_email"
        }

    if any(word in text for word in read_keywords):
        return {
            "intent": "read_email"
        }

    if any(word in text for word in exit_keywords):
        return {
            "intent": "exit"
        }

    return {
        "intent": "unknown"
    }