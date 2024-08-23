from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

model = genai.GenerativeModel('models/gemini-1.5-pro')

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image Demo")

st.header("Gemini Application")

input=st.text_input("Input prompt: ",key="input")
upload_file=st.file_uploader("Choose An Image...", type=["jpg","jpeg","png"])
image=""

if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about image")

if submit:    
    response=get_gemini_response(input,image)
    st.subheader("The Reason is")
    st.write(response)
