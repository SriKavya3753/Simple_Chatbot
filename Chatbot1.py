import streamlit as st
import google.generativeai as genai
API_KEY = "AIzaSyBgndmpUIay-E7vWzr4kQK0RXisCjbg9T8"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
  st.session_state.chat = model.start_chat(history=[])
st.title(" ChatBot - Your AI Assistant")  
st.write('This is an AI Chatbot to solve your queries....')

if "messages" not in st.session_state:
  st.session_state.messages = []
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt := st.chat_input("Say something..."):
  st.session_state.messages.append({"role":"user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response = st.session_state.chat.send_message(prompt)

  st.session_state.messages.append({"role":"assistant", "content": response.text})
  with st.chat_message("assistant"):
    st.markdown(response.text)
