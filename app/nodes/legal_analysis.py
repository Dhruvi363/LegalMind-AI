from app.state import LegalState
from app.config import llm

def legal_analysis(state: LegalState):

    prompt = f"""
    You are an Indian legal assistant.

    User Query:
    {state['user_query']}

    Relevant IPC/BNS Sections:
    {state['ipc_sections']}

    Explain:

    1. Applicable laws
    2. Possible legal remedies
    3. Important considerations
    """

    response = llm.invoke(prompt)

    return {
        "analysis": response.content
    }