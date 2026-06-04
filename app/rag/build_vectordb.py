import json
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

with open("app/rag/ipc.json", "r", encoding="utf-8") as f:
    ipc_data = json.load(f)

documents = []

for item in ipc_data:
    documents.append(
        Document(

            page_content=f"""
Section: {item['Section']}
Title: {item['section_title']}
Content: {item['section_desc']}
""",
metadata={
    "section": item["Section"],
    "title": item["section_title"],
    "chapter": item["chapter"],
    "chapter_title": item["chapter_title"]
}
            
            
        )
    )

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="app/rag/vectordb"
)

print(f"Stored {len(documents)} sections successfully.")