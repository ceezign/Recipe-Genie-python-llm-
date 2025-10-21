# 🍳  Recipe Genie

AI Recipe Genie is an intelligent recipe generator web app built with Streamlit and Hugging Face Mixtral-8x7B-Instruct model.  
It allows users to input ingredients, select cuisine type and dietary preferences, and instantly generate creative, healthy, and tasty recipes using AI.

---

## 🚀 Features

- 🧠 AI-Powered Recipe Generation: Generates unique recipes with instructions based on your input.
- 🥗 Cuisine & Dietary Options: Choose from multiple cuisines (African, Asian, Italian, etc.) and dietary styles (Vegan, Keto, Low-Carb, etc.).
- 🎨 Modern Gradient UI: A sleek, frosted glass design with gradient backgrounds.
- ⚙️ Modular Structure: Code organized into multiple files for better readability and maintainability.
- 📦 Environment Variable Support: Uses .env for API tokens and sensitive configuration.

---

---
## Recipe Genie Screenshot
![Recipe Genie Screenshot ](assets/images/screenshot1.png)
![Recipe Genie Screenshot ](assets/images/screenshot2.png)
![Recipe Genie Screenshot ](assets/images/screenshot4.png)
![Recipe Genie Screenshot ](assets/images/screenshot5.png)
---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository
git clone https://github.com/your-username/ai-recipe-genie.git
cd ai-recipe-genie

### 2️⃣ Create and Activate Virtual Environment
python -m venv .venv
# Activate it
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Create a .env File

In the root folder, create a .env file and add your Hugging Face token like this:
HUGGINGFACE_API_TOKEN=your_huggingface_token_here

You can create a new token at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).  
Make sure it has "read" and "inference" permissions.

### 5️⃣ Run the App
streamlit run app.py

The app will open automatically in your browser.

---

## 💡 Example Use

1. Enter ingredients (e.g. *chicken, rice, spinach*).  
2. Choose a cuisine (e.g. *African*).  
3. Select dietary preference (e.g. *High-Protein*).  
4. Click Generate Recipes and let the AI work its magic.

---

## 🧠 Tech Stack

- Python 3.10+
- Streamlit – for the web UI
- LangChain + HuggingFaceEndpoint – for connecting to the AI model
- Mixtral-8x7B-Instruct – the AI model generating the recipes
- dotenv – for environment variable management

---

## 🖌️ UI Preview

A modern, frosted-glass UI with gradient background and glowing buttons.

![Preview Screenshot](assets/ui-preview.png)

---

## 🛠️ Future Improvements

- 📱 Add image generation for recipe preview  
- 💾 Allow saving or downloading recipes as PDF  
- 🧑‍🍳 Add a “Surprise Me” mode for random recipes  
- 🗣️ Voice-to-text ingredient input  

---

## 👨‍💻 Author

Atunde Toheeb Ayomide (Jiggy)  
📍 Lagos, Nigeria  
📧 [atundetoheeb1@gmail.com](mailto:atundetoheeb1@gmail.com)  
🔗 [GitHub](https://github.com/ceezign) | [LinkedIn](https://www.linkedin.com/in/atunde-toheeb-551826313)

---

## 🪪 License

This project is open source and available under the MIT License.