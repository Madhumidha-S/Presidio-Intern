from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import subprocess

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "rag_docs"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL = "mistral"

embedder = SentenceTransformer(EMBED_MODEL_NAME)
client = PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(name=COLLECTION_NAME)

def embed_query(text: str):
    return embedder.encode([text], show_progress_bar=False).tolist()[0]

def ask_ollama(context: str, question: str):
    """Send the context and question to an Ollama model."""
    prompt = f"""
You are a helpful assistant. 
Answer only using the provided context.
If the answer is not in the context, reply: 'Information not available in the knowledge base.'

Context:
{context}

Question: {question}
"""
    result = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").strip()

SAMPLE_QA = [
   {"q": "What is the RIP Message Format?", "a": "The type of message: request (1) and response (2)."},
   {"q": "What is Poison Reverse?", "a": "Information received is used to update routing table and then passed out to all interface."},
   {"q": "What is the use of Update Message?", "a": "To withdraw destinations that have been advertised previously and announce a route to a new destination."},
   {"q": "What is CIDR?", "a": "IP Addressing method which allows flexible subnetting by describing networks using prefix notation."},
   {"q": "What is Subnet Mask?", "a": "Subnet Mask is like an IP address but used only for internal usage."}
]

def evaluate_rag(samples):
   print("\n=== RAG Evaluation ===")
   for i, qa in enumerate(samples, start=1):
       print(f"\n[{i}] Q: {qa['q']}")
       query_emb = embed_query(qa['q'])
       results = collection.query(query_embeddings=[query_emb], n_results=3)
       context = ""
       for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
           context += f"({meta['source']} - Page {meta['page']}): {doc}\n"
       answer = ask_ollama(context, qa['q'])
       print("Expected:", qa['a'])
       print("Generated:", answer)
       print("-" * 50)

while True:
    query = input("\nEnter your question (or 'exit' to quit): ")
    if query.lower() in ["exit", "quit"]:
        break
    query_emb = embed_query(query)
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=3
    )
    print("\n--- Top 3 Retrieved Chunks ---")
    context = ""
    for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0]), start=1):
        print(f"\n[{i}] Source: {meta['source']}, Page: {meta['page']}, Chunk: {meta['chunk']}")
        print(doc[:300], "...")
        context += f"\n[{i}] ({meta['source']} - Page {meta['page']}): {doc}\n"

    print("\n--- Answer ---")
    answer = ask_ollama(context, query)
    print(answer)
    

if __name__ == "__main__":
    # --- 1. Evaluate Sample Q/A ---
    print("=== Running Example Q/A Evaluation ===")
    evaluate_rag(SAMPLE_QA)

    # --- 2. Interactive Query Loop ---
    while True:
        query = input("\nEnter your question (or 'exit' to quit): ")
        if query.lower() in ["exit", "quit"]:
            break
        query_emb = embed_query(query)
        results = collection.query(query_embeddings=[query_emb], n_results=3)
        print("\n--- Top 3 Retrieved Chunks ---")
        context = ""
        for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0]), start=1):
            print(f"[{i}] Source: {meta['source']}, Page: {meta['page']}, Chunk: {meta['chunk']}")
            print(doc[:300], "...\n")
            context += f"[{i}] ({meta['source']} - Page {meta['page']}): {doc}\n"

        # --- 3. Generate answer using Prompt ---
        print("\n--- Answer ---")
        answer = ask_ollama(context, query)
        print(answer)
