from langgraph.graph import StateGraph, END

from app.state import LegalState

from app.nodes.classifier import classify_case
from app.nodes.ipc_retriever import ipc_retriever
from app.nodes.legal_analysis import legal_analysis
from app.nodes.drafting import draft_document

builder = StateGraph(LegalState)

builder.add_node("classifier", classify_case)
builder.add_node("retriever", ipc_retriever)
builder.add_node("analysis", legal_analysis)
builder.add_node("drafting", draft_document)

builder.set_entry_point("classifier")

builder.add_edge("classifier", "retriever")
builder.add_edge("retriever", "analysis")
builder.add_edge("analysis", "drafting")
builder.add_edge("drafting", END)

graph = builder.compile()