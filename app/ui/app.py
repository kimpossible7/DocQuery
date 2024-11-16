import streamlit as st
import requests

st.title("Document Question Answering Bot")
st.write("Upload a document and provide your questions to get answers.")

# Upload file
uploaded_file = st.file_uploader("Choose a file (PDF or JSON)", type=["pdf", "json"])

# Input questions
questions = st.text_area("Enter your questions (one per line):")

if st.button("Get Answers"):
    if not uploaded_file or not questions.strip():
        st.error("Please upload a file and provide at least one question.")
    else:
        # Send to FastAPI
        files = {"document": uploaded_file.getvalue()}
        data = {"questions": questions.strip().split("\n")}
        response = requests.post("http://localhost:8000/question-answer/", json=data, files=files)

        if response.status_code == 200:
            for result in response.json():
                st.write(f"**Q:** {result['question']}\n**A:** {result['answer']}")
        else:
            st.error("Error: " + response.json().get("detail", "Unknown error"))
