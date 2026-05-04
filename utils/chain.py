from langchain.chains import RetrievalQA

def build_chain(llm, retriever, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )
