import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/detectLanguage"


def main():
    st.title("Language Detector")

    st.text_input("Text", key="text")

    if st.button("Detect"):

        if not st.session_state.text.isalpha():
            st.error("Input should be text")
        
        else:
            text_json = {"text":st.session_state.text}

            headers = {'Content-Type': 'application/json'}
            response = requests.post(API_URL, json=text_json)

            st.write(f"Language: {response.json().get('language')}")
    
if __name__ == "__main__":
    main()