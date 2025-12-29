import streamlit as st
from google import genai
from google.genai import types
import os

# Get API key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Create client
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI tutor for freshers.
Explain concepts step-by-step.
Use simple language.
Give real-world examples.
If needed, give a short code example.
Ask one follow-up question.
"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

st.title("🎓 Gemini AI Tutor")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    response = chat.send_message(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", response.text))

for role, msg in st.session_state.messages:
    st.markdown(f"**{role}:** {msg}")
