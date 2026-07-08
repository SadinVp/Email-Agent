from llm.parser import parse_response

response = """
{
    "tool":"delete_everything",
    "arguments":{}
}
"""

decision = parse_response(response)

print(decision)