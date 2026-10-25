import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

def create_llm() -> ChatDeepSeek:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY is not set in the environment variables.")

    return ChatDeepSeek(
        api_key=api_key,
        model="deepseek-chat",
        temperature=0.7,
    )