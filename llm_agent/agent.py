import os
from dotenv import load_dotenv
from google import genai


class GeminiAgent:

    def __init__(self):

        # Load API key from .env
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("Gemini API Key not found!")

        # Create Gemini client
        self.client = genai.Client(
            api_key=api_key
        )

        # Current model available to our API key
        self.model = "gemini-3.5-flash"

    def ask(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text