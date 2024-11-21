import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#Load environment variable
load_dotenv()

#configure streamlit page setting
st.set_page_config(
    page_title="Gemini Pro ChatBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#Set up google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot title on the page
st.title("Gemini Pro - ChatBot")

# Display the Chat History
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro....")
if user_prompt:
   st.chat_message("user").markdown(user_prompt)

   gemini_response = st.session_state.chat_session.send_message(user_prompt)

   with st.chat_message("assistant"):
       st.markdown(gemini_response.text)

