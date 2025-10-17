
def clean_ingredients(ingredients_text):

    ingredients = [ingredient.strip() for ingredient in ingredients_text.split(",")]
    ingredients = [ingredient for ingredient in ingredients if ingredient and
                   len(ingredient) > 0]
    return list(set(ingredients))   # remove duplicates


def validate_ingredients(ingredients):
    if not ingredients:
        return False, "Please enter at least one ingredient"

    if len(ingredients) > 20:
        return False, "Too many ingredients (max 20)"

    return True, None

def format_ingredients_for_llm(ingredients):
    """Format ingredients for LLM prompt"""
    return ", ".join(ingredients)