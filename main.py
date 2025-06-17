import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Languages List
languages = [
    "English", "Urdu", "Hindi", "Arabic", "Bengali", "Punjabi", "Tamil", "Telugu", "Gujarati",
    "Marathi", "Kannada", "Malayalam", "Odia", "Assamese", "Nepali", "Sinhala", "Pashto", "Persian",
    "French", "German", "Spanish", "Portuguese", "Italian", "Dutch", "Swedish", "Norwegian", "Danish",
    "Finnish", "Russian", "Ukrainian", "Polish", "Czech", "Slovak", "Romanian", "Hungarian", "Bulgarian",
    "Greek", "Turkish", "Hebrew", "Chinese (Simplified)", "Chinese (Traditional)", "Japanese", "Korean",
    "Thai", "Vietnamese", "Indonesian", "Filipino", "Malay", "Swahili", "Zulu", "Xhosa"
]

# Streamlit UI
st.set_page_config(page_title="Translator by Rimza", layout="centered")
st.title("AI Languages Translator 🌐")
st.write("Created by **Rimza Asad** – Translate your English text into various languages using Gemini AI.")

# User Inputs
text = st.text_area("Enter text in English", height=200, placeholder="Type your text here...")
lang = st.selectbox("Select Language", languages)
btn = st.button("Translate")

# Translation Logic
if btn and text:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Translate the following text into {lang}:\n\n{text}"
        response = model.generate_content(prompt)

        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

