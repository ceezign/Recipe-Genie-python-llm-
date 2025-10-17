import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL= os.getenv("OPENAI_MODEL")
TEMPERATURE = float(os.getenv("TEMPERATURE"))

FAVOURITES_FILE = "data/favourites.json"

DIETARY_OPTIONS = ["None", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo"]

PAGE_CONFIG = {
    "page_title": "🍳 AI Recipe Generator",
    "page_icon": "🍳",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

RECIPES_PER_GENERATION = 3
SIDEBAR_WIDTH = 300