import json

from src.ai_client import GeminiClient


class AIJudge:
    def __init__(self, client : GeminiClient):
        self.client = client

    def evaluate(self, user_prompt, response, acceptance_criteria):
        judge_prompt = f"""
        Grade this AI response based on criteria.
        Prompt: {user_prompt}
        Response: {response}
        Criteria:{acceptance_criteria}
        Return in JSON format only: {{"verdict":"PASS/FAIL, "reason": "why"}}
        """
        result = self.client.ask(judge_prompt)
        cleaned_result = result.lstrip('```json').rstrip('```')
        try:
            json_result = json.loads(cleaned_result)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None  # or handle the error as needed

            # Return the JSON object (now you can access the verdict and reason from the dictionary)
        return json_result
        