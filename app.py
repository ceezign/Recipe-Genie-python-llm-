# app.py
import streamlit as st
from src.ui import show_generator_ui, show_about_ui, show_saved_ui, load_css

load_css()

st.set_page_config(page_title="AI Recipe Genie", page_icon="🍳", layout="wide")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3655/3655682.png", width=100)
    choice = st.radio("Navigate", ["Generate", "Saved", "About"])

if choice == "Generate":
    show_generator_ui()
elif choice == "Saved":
    show_saved_ui()
else:
    show_about_ui()