from dotenv import load_dotenv
from app.state import LegalState

load_dotenv()

from app.config import llm

def draft_document(state: LegalState):

    prompt = f"""
    Based on this legal issue:

    {state['user_query']}

    And this analysis:

    {state['analysis']}

    Draft a formal complaint letter.
    """

    response = llm.invoke(prompt)

    return {
        "draft_document": response.content
    }