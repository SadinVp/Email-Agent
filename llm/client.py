from openai import OpenAI
from config import OPENROUTER_API_KEY
from llm.prompt import build_system_prompt
from llm.parser import parse_response

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


MODEL = "openrouter/free"

def analyze(user_input: str):

    system_prompt = build_system_prompt()

    response = client.chat.completions.create(

        model=MODEL,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0
    )
    print(response)
    return parse_response(response.choices[0].message.content)