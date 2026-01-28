import os
from dotenv import load_dotenv

load_dotenv()


LLM_MODE = os.getenv("LLM_MODE")

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("MODEL_NAME")
