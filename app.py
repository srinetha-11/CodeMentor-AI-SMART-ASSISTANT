import streamlit as st
from openai import OpenAI
import os

# -----------------------------
# Configure your OpenAI API Key
# -----------------------------
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    st.error("Please set your OPENAI_API_KEY environment variable.")
    st.stop()

client = OpenAI(api_key=API_KEY)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="💻",
    layout="wide"
)

st.title("💻 CodeMentor AI - Smart Programming Assistant")
st.write("Analyze, review, explain and improve your code using AI.")

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS"
    ]
)

task = st.selectbox(
    "Choose Task",
    [
        "Explain Code",
        "Review Code",
        "Find Bugs",
        "Optimize Code",
        "Generate Comments"
    ]
)

code = st.text_area(
    "Paste your code here",
    height=350
)

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please enter some code.")
    else:

        prompt = f"""
You are an expert software engineer.

Language:
{language}

Task:
{task}

Code:
{code}

Provide:
1. Explanation
2. Errors (if any)
3. Suggestions
4. Better Version (if applicable)
"""

        with st.spinner("Analyzing..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role":"system",
                        "content":"You are an expert programming mentor."
                    },
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

        st.success("Analysis Complete")
        st.markdown(answer)

st.markdown("---")

st.subheader("Features")

st.write("✔ Code Explanation")
st.write("✔ Code Review")
st.write("✔ Bug Detection")
st.write("✔ Optimization Suggestions")
st.write("✔ Auto Documentation")

st.markdown("---")

st.caption("Developed using Python + Streamlit + OpenAI")