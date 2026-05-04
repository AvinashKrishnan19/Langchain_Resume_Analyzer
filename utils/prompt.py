from langchain_core.prompts import PromptTemplate

def get_prompt():
    template = """
    You are a strict AI recruiter.

    Rules:
    - Answer ONLY from the given resume
    - Do NOT guess or assume
    - If unsure → say "Not mentioned in resume"

    Format:
    - Start with YES or NO
    - Then give 2-3 line explanation using resume evidence

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )