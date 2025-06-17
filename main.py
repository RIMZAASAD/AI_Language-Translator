import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set Gemini key
genai.configure(api_key=api_key)

# Supported Languages
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

text = st.text_area("Enter English text to translate:", height=150)
lang = st.selectbox("Select target language:", languages)
btn = st.button("Translate")

if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following text to {lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")