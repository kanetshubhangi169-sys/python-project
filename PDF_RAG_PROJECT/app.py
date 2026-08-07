"""
app.py
------
Streamlit UI for the PDF RAG Question-Answering system.

Pipeline triggered by this UI:
  1. User uploads one or more PDFs.
  2. On "Process PDFs": extract text (with page metadata) -> split
     into chunks -> embed with Hugging Face -> store in ChromaDB.
  3. User asks a question in a text box.
  4. The retriever fetches the most relevant chunks from ChromaDB,
     Llama 3.2:3B (via Ollama) generates an answer grounded in them,
     and the UI displays the answer plus the exact source chunks
     and page numbers used.

Run with:  streamlit run app.py
"""

import uuid

import streamlit as st

from src import pdf_processor, vector_store, qa_engine


st.set_page_config(page_title="PDF Q&A with RAG", page_icon="📄", layout="wide")


# ----------------------------------------------------------------------
# Session state initialization
# ----------------------------------------------------------------------
# We keep the vector store, QA chain, and a per-session collection name
# in st.session_state so they persist across Streamlit reruns (Streamlit
# reruns the whole script on every interaction, so anything expensive
# -- like embeddings or the loaded LLM -- must be cached in session state
# rather than rebuilt every time).
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "collection_name" not in st.session_state:
    st.session_state.collection_name = f"session_{uuid.uuid4().hex[:8]}"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of {question, answer, sources}


# ----------------------------------------------------------------------
# Sidebar: upload + process PDFs
# ----------------------------------------------------------------------
with st.sidebar:
    st.header("📁 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True,
    )

    process_clicked = st.button("🚀 Process PDFs", type="primary", disabled=not uploaded_files)

    if process_clicked and uploaded_files:
        with st.spinner("Extracting text from PDFs..."):
            documents = pdf_processor.load_pdfs(uploaded_files)

        with st.spinner("Splitting text into chunks..."):
            chunks = pdf_processor.split_documents(documents)

        with st.spinner("Generating embeddings and storing in ChromaDB..."):
            vectorstore = vector_store.build_vectorstore(
                chunks, collection_name=st.session_state.collection_name
            )
            retriever = vector_store.get_retriever(vectorstore)

        with st.spinner("Connecting to Ollama (Llama 3.2:3B)..."):
            qa_chain = qa_engine.build_qa_chain(retriever)

        st.session_state.vectorstore = vectorstore
        st.session_state.qa_chain = qa_chain
        st.session_state.chat_history = []

        st.success(f"Processed {len(uploaded_files)} file(s) into {len(chunks)} chunks. Ready for questions!")

    st.divider()
    st.caption(
        "**Requirements:**\n"
        "- Ollama running locally (`ollama serve`)\n"
        "- Model pulled: `ollama pull llama3.2:3b`\n"
        "- Embeddings run locally via Hugging Face (no API key needed)"
    )


# ----------------------------------------------------------------------
# Main area: ask questions
# ----------------------------------------------------------------------
st.title("📄 PDF Question Answering (RAG)")
st.write(
    "Upload PDFs in the sidebar, click **Process PDFs**, then ask questions "
    "about their content below. Answers are grounded in the retrieved passages."
)

if st.session_state.qa_chain is None:
    st.info("👈 Upload and process at least one PDF to get started.")
else:
    question = st.text_input("Ask a question about your documents:")
    ask_clicked = st.button("🔍 Get Answer")

    if ask_clicked and question.strip():
        with st.spinner("Retrieving relevant passages and generating answer..."):
            result = qa_engine.answer_question(st.session_state.qa_chain, question)

        st.session_state.chat_history.insert(
            0, {"question": question, "answer": result["answer"], "sources": result["sources"]}
        )

    # Display conversation history, most recent first
    for turn in st.session_state.chat_history:
        st.markdown(f"### ❓ {turn['question']}")
        st.markdown(f"**Answer:** {turn['answer']}")

        with st.expander(f"📚 View {len(turn['sources'])} source chunk(s) used"):
            for i, src in enumerate(turn["sources"], start=1):
                st.markdown(f"**Source {i}** — `{src['source']}`, page **{src['page']}**")
                st.text(src["content"])
                st.divider()

        st.divider()