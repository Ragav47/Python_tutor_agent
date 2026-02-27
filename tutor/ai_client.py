from openai import OpenAI
from config import OPENROUTER_API_KEY, BASE_URL

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)