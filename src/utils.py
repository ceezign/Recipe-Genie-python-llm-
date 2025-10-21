import re
import time
from typing import List

def build_prompt(ingredients: str, dietary: str, cuisine: str, recipes_count: int =3) -> str:
    ingredients_clean = sanitize_ingredients(ingredients)
    prompt = (
        f"You are a friendly, precise chef. Create {recipes_count} distinct "
        f"recipes using these ingredients.\n\n"
        f"Ingredients: {ingredients_clean}\n"
        f"Dietary Preferences: {dietary}\n"
        f"Cuisine Style: {cuisine}\n\n"
        "For each recipe include:\n"
        "- Recipe Name\n"
        "- Short Description (2 sentences)\n"
        "- Ingredients with quantities\n"
        "- Step-by-step numbered instructions\n"
        "- Total cooking time\n"
        "- Difficulty (Easy/Medium/Hard)\n\n"
        'Label each recipe "RECIPE 1:", "RECIPE 2:", etc. Keep output clean and human-readable.'
    )
    return prompt

def sanitize_ingredients(raw: str) -> str:
    """remove extra whitespace, convert seperators to commas"""
    if not raw:
        return ""
    cleaned = re.sub(r'[\n;]+', ',', raw.strip())
    cleaned = re.sub(r'\s*, \s*', ', ', cleaned)
    return cleaned

def parse_recipes(raw: str) -> List[str]:
    if not raw:
        return []
    # Normalize newlines
    raw = raw.strip()
    # Try to split on "RECIPE" headers (case-insensitive)
    parts = re.split(r'(?i)RECIPE\s*\d*\s*:?', raw)
    recipes = [p.strip() for p in parts if p.strip()]
    # If splitting produced nothing, fallback to chunking by double newlines
    if not recipes:
        recipes = [p.strip() for p in raw.split("\n\n") if p.strip()]
    return recipes

def simple_retry(fn, retries=2, delay=1, backoff=2, *args, **kwargs):
    last_exc = None
    d = delay
    for i in range(retries + 1):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            last_exc = e
            if i == retries:
                raise
            time.sleep(d)
            d *= backoff




















