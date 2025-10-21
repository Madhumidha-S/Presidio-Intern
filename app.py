from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import subprocess

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "rag_docs"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL = "mistral"

app = FastAPI(title="RAG API", version="1.0")
embedder = SentenceTransformer(EMBED_MODEL_NAME)
client = PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(name=COLLECTION_NAME)

class QueryRequest(BaseModel):
    question: str

def embed_query(text: str):
    return embedder.encode([text], show_progress_bar=False).tolist()[0]

def ask_ollama(context: str, question: str):
    prompt = f"""
You are a helpful assistant.
Answer only using the provided context.
If the answer is not in the context, reply: 'Information not available in the knowledge base.'
Context:
{context}

Question: {question}
"""
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {e}")

@app.post("/ask")
def ask_question(req: QueryRequest):
    try:
        query_emb = embed_query(req.question)
        results = collection.query(query_embeddings=[query_emb], n_results=3)

        context = ""
        sources = []
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            context += f"({meta['source']} - Page {meta['page']}): {doc}\n"
            sources.append(meta)

        answer = ask_ollama(context, req.question)
        return {"answer": answer, "sources": sources}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
