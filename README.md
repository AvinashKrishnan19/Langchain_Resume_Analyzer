# 📄 AI Resume Analyzer (LangChain RAG Project)

An AI-powered Resume Analyzer that enables recruiters to evaluate candidates by asking natural language questions.  
Built using **LangChain (RAG architecture)**, this system extracts insights directly from resumes and provides accurate, context-aware answers.

---

## 🚀 Demo

👉 Upload a resume → Ask questions → Get AI-generated answers based on resume content

---

## 🎯 Key Features

- 📤 Upload PDF resumes
- 💬 Ask recruiter-style questions
- 🧠 Context-aware answers using RAG
- ✅ YES/NO answers with explanation
- ⚡ Fast semantic search using FAISS
- 🎨 Clean and interactive Streamlit UI
- 🔒 No paid APIs (runs locally with HuggingFace models)

---

## 🧠 How It Works

1. Resume is uploaded and parsed using PyPDF
2. Text is split into meaningful chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. Relevant context is retrieved based on query
6. FLAN-T5 model generates the final answer

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **FAISS (Vector Database)**
- **HuggingFace Transformers (FLAN-T5)**
- **Sentence Transformers (Embeddings)**
- **Streamlit (UI)**

---

## 📂 Project Structure


LangchainResume/
│
├── app.py
├── config.py
├── requirements.txt
│
├── services/
│ └── resume_service.py
│
├── utils/
│ ├── loader.py
│ ├── splitter.py
│ ├── embeddings.py
│ ├── vectorstore.py
│ ├── llm.py
│ ├── prompt.py
│ └── chain.py
│
├── .streamlit/
│ └── config.toml
│
└── README.md


---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
2. Install dependencies
pip install -r requirements.txt
3. Run the application
streamlit run app.py

💡 Example Questions
Does the candidate have experience in AI?
What are the key technical skills?
What projects has the candidate worked on?
Is the candidate suitable for an ML Engineer role?

🎯 Use Case

This project is designed for HRs and recruiters to:

Quickly screen multiple resumes
Validate candidate experience
Extract key skills automatically
Make faster and more informed hiring decisions

🧠 Learning Outcomes
Built an end-to-end RAG pipeline using LangChain
Implemented semantic search with FAISS
Applied prompt engineering for controlled outputs
Developed a real-world AI application for recruitment
Gained hands-on experience with LLMs and embeddings

🚀 Future Improvements
Candidate scoring system (/10)
Skill gap analysis vs job role
Multiple resume comparison
Chat history memory
Cloud deployment (Streamlit Cloud)

📌 Notes
Uses local HuggingFace models (no API cost)
Accuracy depends on model capability (FLAN-T5)

🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Avinash Krishnan
AI/ML Enthusiast | AI Developer
