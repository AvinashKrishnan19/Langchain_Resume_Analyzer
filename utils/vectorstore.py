from langchain_community.vectorstores import FAISS

def create_vectorstore(docs, embeddings):

    db = FAISS.from_documents(docs, embeddings)

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 6}
    )

    return retriever
