
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Vision-Able AI", page_icon="♿")
st.title("Vision-Able: Accessibility AI Agent")
st.write("Welcome! Let's build the future of accessibility.")

# API Key Kontrolü
if not os.getenv("OPENAI_API_KEY"):
    st.error("Lütfen .env dosyasına OPENAI_API_KEY ekleyin!")
