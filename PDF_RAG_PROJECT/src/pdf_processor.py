"""
pdf_processor.py
----------------
Responsible for:
  1. Taking Streamlit-uploaded PDF file objects and writing them to a
     temporary location on disk (LangChain's PDF loaders need a file path).
  2. Extracting text page-by-page, preserving `source` (filename) and
     `page` metadata for every page -- this is what lets us later show
     "Source: report.pdf, Page 4" next to a retrieved chunk.
  3. Splitting the extracted pages into overlapping chunks sized for
     embedding + retrieval.
"""

import os
import tempfile
from typing import List

from langchain_community.document_loaders import PyPDFLoader

try:
    # Newer langchain versions moved Document into langchain_core
    from langchain_core.documents import Document
except ImportError:
    from langchain.docstore.document import Document

try:
    # Newer langchain versions split text splitters into their own package
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    # Older langchain versions keep it inside the main package
    from langchain.text_splitter import RecursiveCharacterTextSplitter

from . import config


def load_pdfs(uploaded_files) -> List[Document]:
    """
    Convert Streamlit UploadedFile objects into a list of LangChain
    Document objects (one per PDF page), each carrying metadata:
        - source: original filename
        - page:   1-indexed page number

    Streamlit gives us in-memory file objects, but PyPDFLoader expects
    a real file path, so each upload is first written to a temp file.
    """
    all_documents: List[Document] = []

    for uploaded_file in uploaded_files:
        # Write the uploaded bytes to a temporary .pdf file on disk
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            tmp_path = tmp_file.name

        try:
            loader = PyPDFLoader(tmp_path)
            pages = loader.load()  # one Document per page, page numbers are 0-indexed by default

            for page_doc in pages:
                # Normalize metadata: use the real filename, make page 1-indexed
                page_doc.metadata["source"] = uploaded_file.name
                page_doc.metadata["page"] = page_doc.metadata.get("page", 0) + 1
                all_documents.append(page_doc)
        finally:
            os.remove(tmp_path)  # always clean up the temp file

    return all_documents


def split_documents(documents: List[Document]) -> List[Document]:
    """
    Split page-level documents into smaller overlapping chunks.

    Why chunk?
      - Embedding models and LLM context windows work best with short,
        semantically focused passages rather than whole pages.
    Why overlap?
      - Prevents losing meaning for sentences that fall right on a
        chunk boundary.

    RecursiveCharacterTextSplitter tries to split on paragraph/sentence
    boundaries first, falling back to smaller separators, which keeps
    chunks more coherent than a naive fixed-length cut.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    # split_documents preserves each source Document's metadata on every
    # resulting chunk, so `source` and `page` survive the split.
    chunks = splitter.split_documents(documents)
    return chunks