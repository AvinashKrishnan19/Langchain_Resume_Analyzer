from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from config import LLM_MODEL

def get_llm():
    pipe = pipeline(
        "text2text-generation",
        model=LLM_MODEL,
        max_new_tokens=300
    )
    return HuggingFacePipeline(pipeline=pipe)

