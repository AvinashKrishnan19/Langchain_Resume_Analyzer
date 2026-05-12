import streamlit as st
from services.resume_service import process_resume

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

/* Main Background */
.main {
    background-color: #0E1117;
}

/* Main Title */
.title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #4CAF50;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #B0B0B0;
    font-size: 18px;
    margin-bottom: 40px;
}

/* Upload + Input Box */
.stFileUploader,
.stTextInput {
    background-color: #1E1E1E;
    padding: 10px;
    border-radius: 12px;
}

/* Answer Box */
.answer-box {
    background-color: #1E1E1E;
    padding: 22px;
    border-radius: 12px;
    border-left: 6px solid #4CAF50;
    color: white;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 20px;
}

/* Button */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}

/* Button Hover */
.stButton>button:hover {
    background-color: #45a049;
    color: white;
}

/* Input Box */
.stTextInput>div>div>input {
    border-radius: 10px;
    font-size: 16px;
}

/* Sidebar */
.css-1d391kg {
    background-color: #161A1D;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.title("⚙ Dashboard")

    st.markdown("---")

    st.markdown("###  About")
    st.write(
        """
        AI-powered Resume Analyzer built using:
        - LangChain
        - FAISS
        - FLAN-T5
        - Streamlit
        """
    )

    st.markdown("---")

    st.markdown("###  Example Questions")

    st.write("""
    ✔ Does the candidate have AI experience?

    ✔ What are the candidate's key skills?

    ✔ Is the candidate suitable for an ML Engineer role?

    ✔ What projects has the candidate worked on?
    """)

    st.markdown("---")

    st.success(" System Running")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(
    '<div class="title"> AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Recruiter Assistant powered by LangChain & RAG</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

st.markdown("###  Upload Candidate Resume")

uploaded_file = st.file_uploader(
    "",
    type="pdf",
    help="Upload resume in PDF format"
)

# -------------------------------------------------
# QUESTION INPUT
# -------------------------------------------------

st.markdown("###  Ask Recruiter Question")

query = st.text_input(
    "",
    placeholder="e.g. Does the candidate have AI experience?"
)

# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------

analyze = st.button(" Analyze Resume")

# -------------------------------------------------
# PROCESSING
# -------------------------------------------------

if uploaded_file and query and analyze:

    # Save uploaded resume
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Loading animation
    with st.spinner(" AI is analyzing the resume..."):

        qa = process_resume("temp.pdf")

        result = qa.invoke({"query": query})

        answer = result["result"]

        # Keep only first 3 lines
        answer = answer.strip()




    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    st.markdown("## AI Recruiter Insight")

    st.markdown(
        f"""
        <div class="answer-box">
        {answer}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# EMPTY STATE
# -------------------------------------------------

elif analyze:
    st.warning(" Please upload a resume and enter a question.")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: Green;
    text-align: right;
    padding-right: 20px;
    padding-bottom: 10px;
    font-size: 14px;
    font-family: sans-serif;
    z-index: 999;
}
</style>

<div class="footer">
    Built by <b>Avinash Krishnan</b>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)