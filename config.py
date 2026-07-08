import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")