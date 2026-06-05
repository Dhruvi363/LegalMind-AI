from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

_db = None
_embeddings = None

def get_db():
    global _db, _embeddings

    if _db is None:

        if _embeddings is None:
            _embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

        _db = Chroma(
            persist_directory="app/rag/vectordb",
            embedding_function=_embeddings
        )

    return _db

def ipc_retriever(state):
    query = state["user_query"]

    db = get_db()

    docs = db.similarity_search(query, k=3)

    ipc_sections = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "ipc_sections": ipc_sections
    }