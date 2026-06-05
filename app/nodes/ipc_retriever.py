from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Chroma DB
db = Chroma(
    persist_directory="app/rag/vectordb",
    embedding_function=embeddings
)

def ipc_retriever(state):
    query = state["user_query"]

    # Retrieve top matching sections
    docs = db.similarity_search(query, k=5)

    # Combine retrieved results
    ipc_sections = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "ipc_sections": ipc_sections
    }