from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#embeddings = HuggingFaceEmbeddings(
#    model_name="sentence-transformers/all-MiniLM-L6-v2")

db = Chroma(
    persist_directory="app/rag/vectordb",
    #embedding_function=embeddings
)

query = "What is punishment for theft?"

docs = db.similarity_search(query, k=5)
print("Number of docs:", len(docs))

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("-" * 50)
    print(doc.page_content)
    print(doc.metadata)