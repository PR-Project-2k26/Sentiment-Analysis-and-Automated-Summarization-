import streamlit as st
from utils import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("🧠 Text Summarizer")

# Input box
user_input = st.text_area("Enter your text here:", height=200)

# Button
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(user_input)
        
        st.subheader("Summary:")
        st.write(summary)