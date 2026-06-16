<<<<<<< HEAD
#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
from os import system

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI" , layout="wide")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents1")

system_prompt=st.text_area("Define your AI Agent: ", height =70 , placeholder="Type Your system prompt here ......(Eg: Act as Genius )")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:",("Groq","openAI"))

if provider == "Groq":
    select_model=st.selectbox("Select Groq Model",MODEL_NAMES_GROQ)
elif provider =="openAI":
    select_model=st.selectbox("Select OPENAI Model",MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow web serach")

user_query=st.text_area("Enter your Query : ", height =150 , placeholder="Ask Aything")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2 : Connect with backend via URL
        import requests

        payload={
            "model_name" : select_model,
            "model_provider" :provider,
            "system_prompt":system_prompt,
            "messages" : [user_query],
            "allow_search": allow_web_search
            
        }

        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:

                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")












=======
#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
from os import system

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI" , layout="wide")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents1")

system_prompt=st.text_area("Define your AI Agent: ", height =70 , placeholder="Type Your system prompt here ......(Eg: Act as Genius )")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:",("Groq","openAI"))

if provider == "Groq":
    select_model=st.selectbox("Select Groq Model",MODEL_NAMES_GROQ)
elif provider =="openAI":
    select_model=st.selectbox("Select OPENAI Model",MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow web serach")

user_query=st.text_area("Enter your Query : ", height =150 , placeholder="Ask Aything")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2 : Connect with backend via URL
        import requests

        payload={
            "model_name" : select_model,
            "model_provider" :provider,
            "system_prompt":system_prompt,
            "messages" : [user_query],
            "allow_search": allow_web_search
            
        }

        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:

                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")












>>>>>>> a2777adc1253ce55266434222cd2e7e8ad2d7341
