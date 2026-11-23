import streamlit as st

st.title("📄 AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer!")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write("File name:", uploaded_file.name)