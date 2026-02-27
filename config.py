import os

# OpenRouter API Key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter endpoint
BASE_URL = "https://openrouter.ai/api/v1"

# AI Model
MODEL_NAME = "openai/gpt-4o-mini"