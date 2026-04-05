import streamlit as st
st.title("AI Resume Analyzer")
uploaded_file = st.file_uploader("Upload your resume", type = "pdf")

if uploaded_file:
    st.success("Resume uploaded successfully")

import pdfplumber as ppx
if uploaded_file:
    with pp.open(uploaded_file) as pdf:
        text = ""

        for page in pdf.pages:
            text+= page.extract_text()
    st.subheader("Extracted text from Resume")
    st.write(text[:1000])

from google import genai

client = genai.Client(api_key="")

if uploaded_file:
    prompt = f"""
    You are a professional HR Recruiter

    Analyze this resume and provide:
    1. Resume score out of 10
    2. Strengths
    3. Weaknesses
    4. Suggestions to improve the resume

    Resume:
    {text}
    """

    response = client.models.generate_content(
        model = "models/gemini-2.5-flash",
        contents = prompt 
    )

    st.subheader("AI Resume Analysis")

    st.write(response.text)
