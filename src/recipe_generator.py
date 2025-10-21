
from typing import Optional
from src.config import get_hf_client
from src.utils import build_prompt, simple_retry

class RecipeGenerator:
    def __init__(self, model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
                 token: Optional[str] = None):
        self.client = get_hf_client(model=model, token=token)

    def generate(self, ingredients: str, dietary: str = "None",
                 cuisine: str = "Any", recipes_count: int = 3,
                 temperature: float = 0.7, max_tokens: int = 700) -> str:
        prompt = build_prompt(ingredients, dietary, cuisine, recipes_count)
        messages = [
            {"role": "system",
             "content": "You are a helpful chef and nutrition-aware recipe writer."},
            {"role": "user", "content": prompt}
        ]

        def call_model():
            return self.client.chat_completion(messages=messages,
                                               temperature=temperature,
                                               max_tokens=max_tokens)

        # retry wrapper
        response = simple_retry(call_model, retries=2, delay=1, backoff=2)
        # extract text
        try:
            content = response.choices[0].message["content"]
        except Exception:
            content = str(response)
        return content















