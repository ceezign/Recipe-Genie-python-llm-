
from langchain.prompts import PromptTemplate

def get_recipe_prompt():
    """Get the recipe generation prompt template"""
    template = """You are a professional chef and recipe expert. Generate 
                    exactly 3 unique recipes based on these available 
                    ingredients: {ingredients}{dietary_preference}
                    
    For each recipe, provide the response in this EXACT JSON format 
    (return valid JSON only, no markdown):
    {{
        "recipes": [
            {{
                "name": "Recipe Name",
                "description": "Brief description of the dish",
                "ingredients_needed": [
                    "ingredient 1 with quantity",
                    "ingredient 2 with quantity"
                ],
                "instructions": [
                    "Step 1",
                    "Step 2",
                    "Step 3"
                ],
                "cooking_time": "XX minutes",
                "difficulty": "Easy|Medium|Hard",
                "additional_ingredients": ["optional ingredient 1", "optional ingredient 2"],
                "nutritional_info": {{
                    "calories_per_serving": "XXX",
                    "protein": "Xg",
                    "carbs": "Xg",
                    "fat": "Xg"
                }}
            }}
        ]
    }}
    Ensure recipes are diverse, practical, and use the provided ingredients as the base."""

    return PromptTemplate(
        input_variables=["ingredients", "dietary_preference"],
        template=template
    )
