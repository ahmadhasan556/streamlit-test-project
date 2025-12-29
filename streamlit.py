from google import genai
import streamlit as st

client = genai.Client(api_key='AIzaSyA3_ZUhquNtk8mT2yuSKERJrX3gpWKVVhY')


st.title("Medical Chatbot")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask anything")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-2.5-flash', contents=user_input
        )
    st.write(response.text)

#streamlit run 05-b-Streamlit.py
