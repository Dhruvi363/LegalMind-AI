from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.state import LegalState

_retriever = None


def get_retriever():
    global _retriever

    if _retriever is None:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = Chroma(
            persist_directory="app/rag/vectordb",
            embedding_function=embeddings
        )

        _retriever = vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )

    return _retriever


def ipc_retriever(state: LegalState):

    retriever = get_retriever()

    docs = retriever.invoke(
        state["user_query"]
    )

    retrieved_text = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return {
        "ipc_sections": retrieved_text
    }