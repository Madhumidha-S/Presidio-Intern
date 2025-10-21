import os
from typing import List, Dict

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from chromadb import PersistentClient

PDF_FILES = ["./docs/Routing.pdf", "./docs/IP.pdf"]
CHROMA_DIR = "./chroma_db"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

embedder = SentenceTransformer(EMBED_MODEL_NAME)

def hf_embed(texts: List[str]) -> List[List[float]]:
    return embedder.encode(texts, show_progress_bar=False, convert_to_numpy=True).tolist()

# client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_DIR))
client = PersistentClient(path=CHROMA_DIR)
collection_name = "rag_docs"
if collection_name in [c.name for c in client.list_collections()]:
    collection = client.get_collection(collection_name)
else:
    collection = client.create_collection(name=collection_name)

# client.delete_collection(collection_name)
# collection = client.create_collection(name=collection_name)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

documents = []
metadatas = []
ids = []
texts = []

doc_id = 0
for pdf_path in PDF_FILES:
    if not os.path.exists(pdf_path):
        print(f"Warning: {pdf_path} not found, skipping.")
        continue
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    for i, page in enumerate(pages, start=1):
        content = page.page_content if hasattr(page, "page_content") else str(page)
        chunks = splitter.split_text(content)
        for c_idx, chunk in enumerate(chunks, start=1):
            uid = f"doc{doc_id}"
            ids.append(uid)
            texts.append(chunk)
            metadatas.append({"source": os.path.basename(pdf_path), "page": i, "chunk": c_idx})
            doc_id += 1
print(f"Total chunks to embed: {len(texts)}")

BATCH = 64
for i in range(0, len(texts), BATCH):
    batch_texts = texts[i:i+BATCH]
    batch_ids = ids[i:i+BATCH]
    batch_meta = metadatas[i:i+BATCH]
    embeddings = hf_embed(batch_texts)
    collection.add(
        documents=batch_texts,
        metadatas=batch_meta,
        ids=batch_ids,
        embeddings=embeddings
    )

# client.persist()
print("Ingest complete. Chroma persisted to", CHROMA_DIR)
