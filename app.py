import streamlit as st
from services.resume_service import process_resume

st.set_page_config(page_title="Resume Analyzer")
st.title(" AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")
query = st.text_input("Ask recruiter question:")



if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    qa = process_resume("temp.pdf")

    if query:
        with st.spinner("Analyzing resume..."):
            result = qa.invoke({"query": query})
            answer = result["result"]
            answer = "\n".join(answer.strip().split("\n")[:3])

        st.subheader("Answer:")
        st.write(answer)