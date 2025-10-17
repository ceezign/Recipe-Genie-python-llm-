
import json
import os
from datetime import  datetime

FAVORITES_FILE = "data/favourites.json"

def ensure_data_dir():
    """Ensure data directory exists"""
    os.makedirs("data", exist_ok=True)

def load_favourites():
    """Load saved favourite recipe from JSON file"""
    ensure_data_dir()

    if os.path.exists(FAVORITES_FILE):
        try:
            with open(FAVORITES_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_favourites(recipes):
    """Save favourite recipes to JSON FILE"""
    ensure_data_dir()

    with open(FAVORITES_FILE, "w") as file:
        json.dump(recipes, file, indent=2)

def add_favourites(recipe):
    """Add a recipe to favourites"""
    favourites = load_favourites()
    recipe["saved_at"] = datetime.now().isoformat()
    favourites.append(recipe)
    save_favourites(favourites)
    return True

def remove_favourites(index):
    """Remove a favourite recipe by index """
    favourites = load_favourites()
    if 0 <= index < len(favourites):
        favourites.pop(index)
        save_favourites(favourites)
        return True
    return False

def export_favourites():
    """Export favourites as JSON string"""
    favourites = load_favourites()
    return json.dumps(favourites, indent=2)
