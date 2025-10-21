
import streamlit as st
from src.recipe_generator import RecipeGenerator
from src.utils import parse_recipes
from pathlib import Path

CSS_PATH = Path("assets/styles.css")

def load_css():
    if CSS_PATH.exists():
        st.markdown(f"<style>{CSS_PATH.read_text()}</style>", unsafe_allow_html=True)

def render_header():
    st.markdown("<div class='top-bar'>"
                   "<h1>🍳 Recipe Genie</h1>"
                    "<div class='small-muted'>"
                        "Turn ingredients into delicious recipes — fast."
                    "</div>"
                "</div>", unsafe_allow_html=True)

def show_generator_ui():
    load_css()
    render_header()

    st.markdown("### Ingredients & Preferences")
    cols = st.columns([2, 1])
    with cols[0]:
        ingredients = st.text_area("Your ingredients (comma-separated)",
                                   placeholder="e.g., chicken, rice, tomatoes,",
                                   height=140)

    with cols[1]:
        dietary = st.selectbox("Dietary", ["None", "Vegetarian", "Vegan",
                                           "Gluten-Free", "Keto", "Paleo"])
        cuisine = st.selectbox("Cuisine", ["Any", "Italian", "Mexican", "Asian",
                                           "Mediterranean", "Indian", "American"])
        recipes_count = st.slider("How many recipes", 1, 5, 3)
        temp = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.05)

    generate = st.button("Generate recipes", help="Use AI to generate recipes",
                         key="generate_btn")

    if generate:
        if not ingredients.strip():
            st.warning("Please enter at least one ingredient.")
            return
        with st.spinner("Generating — Chef Jiggy is preparing your recipes...."):
            rg = RecipeGenerator()
            raw = rg.generate(ingredients=ingredients, dietary=dietary, cuisine=cuisine,
                              recipes_count=recipes_count, temperature=temp)
            st.session_state.generated_raw = raw
            st.success("Recipes generated!")

    # show results
    if "generated_raw" in st.session_state:
        st.markdown("---")
        st.markdown("## Your Recipes")
        recipes = parse_recipes(st.session_state.generated_raw)
        for i, rec in enumerate(recipes, start=1):
            with st.expander(f"Recipe {i}", expanded=True):
                st.markdown(f"<div class='recipe-card'>{rec}</div>", unsafe_allow_html=True)
                # optionally show a placeholder image
                img_col1, img_col2 = st.columns([1, 3])
                with img_col1:
                    # small image placeholder (unsplash random food)
                    st.image(f"https://source.unsplash.com/collection/139386/220x160?sig={i}",
                             width=220)
                with img_col2:
                    if st.button(f"Save Recipe {i}", key=f"save_{i}"):
                        save_recipe_to_file(i, rec)
                        st.success("Saved!")

def save_recipe_to_file(idx: int, content: str):
    # from src.utils import build_prompt
    import json, os
    filename = "saved_recipes.json"
    entry = {"name": f"Recipe {idx}", "content": content,
             "saved_at": st.session_state.get("saved_at", "")}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            arr = json.load(file)
    else:
        arr = []
    arr.append(entry)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(arr, file, indent=2)

def show_saved_ui():
    load_css()
    st.markdown("<h2>Saved Recipes</h2>", unsafe_allow_html=True)
    # from src.utils import load_saved_recipes if False else None    # ensure we don't break import
    import json, os
    fn = "saved_recipes.json"
    if not os.path.exists(fn):
        st.info("No saved recipes yet.")
        return
    with open(fn, "r", encoding="utf-8") as f:
        arr = json.load(f)
    for i, r in enumerate(reversed(arr), start=1):
        with st.expander(f"{r.get('name','Recipe')} — {r.get('saved_at','')}"):
            st.markdown(r.get("content",""))
            if st.button(f"Delete {i}", key=f"del_{i}"):
                arr2 = [x for x in arr if x != r]
                with open(fn, "w", encoding="utf-8") as file:
                    json.dump(arr2, file, indent=2)
                st.success("Deleted")
                st.experimental_rerun()

def show_about_ui():
    load_css()
    st.markdown("## About AI Recipe Genie")
    st.markdown("- Modern UI with recipe cards")
    st.markdown("- Uses Mixtral-Instruct via Hugging Face Inference API")