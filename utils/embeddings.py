from langchain_community.embeddings import HuggingFaceEmbeddings
def get_embeddings():
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2")


