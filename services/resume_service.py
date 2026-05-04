from utils.loader import load_pdf
from utils.splitter import split_docs
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vectorstore
from utils.llm import get_llm
from utils.prompt import get_prompt
from utils.chain import build_chain

def process_resume(file_path):
    docs = load_pdf(file_path)
    chunks = split_docs(docs)

    embeddings = get_embeddings()
    db = create_vectorstore(chunks, embeddings)

    retriever = db.as_retriever()
    llm = get_llm()
    prompt = get_prompt()

    qa_chain = build_chain(llm, retriever, prompt)

    return qa_chain