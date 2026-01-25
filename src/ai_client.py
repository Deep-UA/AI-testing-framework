import os

from dotenv import load_dotenv
from google import genai

from .my_logger import create_logger

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.logger = create_logger("GeminiClientLogger")
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.logger.error("API Key not found! Check your .env file.")
            raise ValueError("API Key not found! Check your .env file.")
        self.client = genai.Client(api_key=api_key)

        self.logger.info("GeminiClient initialized.")



    def ask(self, prompt:str, model: str = "gemini-2.5-flash-lite") -> str:
        try:
            response = self.client.models.generate_content(model=model, contents=prompt)
            self.logger.info(f"Model response: {response.text}")
            return response.text
        except Exception as e:
            self.logger.info(f"Model response: {response.text}")
            return f"Error: {str(e)}"

