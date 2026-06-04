from typing import TypedDict

class LegalState(TypedDict):
    user_query: str
    legal_category: str
    ipc_sections: str
    analysis: str
    draft_document: str