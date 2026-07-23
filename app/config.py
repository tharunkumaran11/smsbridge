import os

from dotenv import load_dotenv

load_dotenv()

GATEWAY_URL = os.getenv("GATEWAY_URL", "")

GATEWAY_TOKEN = os.getenv("GATEWAY_TOKEN", "")

TIMEOUT = int(os.getenv("TIMEOUT", "10"))

API_KEY = os.getenv("API_KEY", "smsbridge123")