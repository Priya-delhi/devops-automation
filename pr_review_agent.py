import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 PR Review Agent (UC9 Demo)")

uploaded_file = st.file_uploader("Upload your Python file", type=["py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    with st.spinner("Reviewing your code with GPT-4..."):
        prompt = f'''
You are an expert code reviewer. Analyze the following Python code for:
- Code smells
- Security issues
- Missing test coverage
- Refactoring suggestions

Here is the code:
{code}
'''

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        review = response['choices'][0]['message']['content']
        st.subheader("💡 GPT-4 Review Suggestions")
        st.markdown(review)
