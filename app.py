from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")


#model=genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

def get_gemini_responses(questions):
    response=model.generate_content(questions)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask The Question")

if submit:
    response=get_gemini_responses(input)
    st.subheader("The Response is:")
    st.write(response)