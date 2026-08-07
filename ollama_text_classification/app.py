import streamlit as st
from ollama import chat

st.set_page_config(
    page_title="Ollama Text Classification",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Ollama Text Classification")

text = st.text_area(
    "Enter your message",
    height=200
)

if st.button("Classify"):

    if text.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    prompt = f"""
You are a spam detection AI.

Classify the message.

Rules:
1. Reply exactly in this format.

Classification: Spam

Reason: <short reason>

OR

Classification: Not Spam

Reason: <short reason>

Message:

{text}
"""

    with st.spinner("Classifying..."):

        response = chat(
            model="llama3.2:1b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response["message"]["content"]

    st.success(result)