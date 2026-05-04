from langchain_community.vectorstores import FAISS

def create_vectorstore(docs, embeddings):
    return FAISS.from_documents(docs, embeddings)
