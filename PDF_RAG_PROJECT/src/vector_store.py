"""
vector_store.py
----------------
Responsible for:
  1. Generating embeddings for text chunks using a Hugging Face
     sentence-transformers model (runs locally, no API key needed).
  2. Storing those embeddings + chunk text + metadata in ChromaDB.
  3. Exposing a LangChain retriever backed by that ChromaDB collection.

Each Streamlit session gets its own fresh, in-memory-backed Chroma
collection built from whatever PDFs the user just uploaded, so
different users / sessions never mix documents.
"""

from typing import List

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

try:
    # Newer langchain versions moved Document into langchain_core
    from langchain_core.documents import Document
except ImportError:
    from langchain.docstore.document import Document

from . import config


def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Load the Hugging Face embedding model.

    all-MiniLM-L6-v2 is a good default: 384-dim vectors, fast on CPU,
    and strong retrieval quality for its size -- ideal for a local
    RAG demo where we don't want to depend on a paid embeddings API.
    """
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},  # cosine similarity works best on normalized vectors
    )


def build_vectorstore(chunks: List[Document], collection_name: str = config.COLLECTION_NAME) -> Chroma:
    """
    Embed all chunks and persist them in a ChromaDB collection.

    Using a fresh `collection_name` per session (see app.py) keeps
    documents from different upload batches isolated from each other.
    """
    embedding_model = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name=collection_name,
        persist_directory=config.CHROMA_PERSIST_DIR,
    )
    return vectorstore


def get_retriever(vectorstore: Chroma, k: int = config.TOP_K):
    """
    Wrap the vector store as a LangChain retriever that returns the
    top-k most semantically similar chunks for a given question.
    """
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})