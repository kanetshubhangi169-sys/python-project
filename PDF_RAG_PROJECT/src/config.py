"""
config.py
---------
Centralized configuration for the PDF RAG application.
Keeping these values in one place makes it easy to tune the
pipeline (chunk size, model choice, retrieval depth, etc.)
without hunting through the rest of the codebase.
"""

# --- Text splitting ---
CHUNK_SIZE = 1000          # characters per chunk
CHUNK_OVERLAP = 150        # overlap between consecutive chunks (preserves context across boundaries)

# --- Embeddings (Hugging Face) ---
# A small, fast, high-quality sentence-embedding model that runs well on CPU.
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# --- Vector store (ChromaDB) ---
CHROMA_PERSIST_DIR = "chroma_db"   # local folder where the vector DB is persisted
COLLECTION_NAME = "pdf_rag_collection"

# --- Retrieval ---
TOP_K = 4                  # number of chunks to retrieve per question

# --- LLM (Ollama) ---
OLLAMA_MODEL = "llama3.2:3b"
OLLAMA_BASE_URL = "http://localhost:11434"   # default local Ollama server
LLM_TEMPERATURE = 0.2       # low temperature -> more grounded, less creative answers

# --- Prompt ---
QA_PROMPT_TEMPLATE = """You are a helpful assistant answering questions using ONLY the
context extracted from the user's uploaded PDF documents.

Rules:
- Answer strictly based on the provided context.
- If the answer is not present in the context, say clearly:
  "I could not find this information in the uploaded documents."
- Be concise and factual. Do not make up information.

Context:
{context}

Question:
{question}

Answer:"""