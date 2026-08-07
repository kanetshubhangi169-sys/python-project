"""
qa_engine.py
------------
Responsible for:
  1. Connecting to a locally running Ollama server and loading the
     Llama 3.2:3B model as the generation LLM.
  2. Wiring the retriever + LLM + prompt together into a
     Retrieval-Augmented Generation (RAG) pipeline: retrieve chunks,
     format them into a prompt, generate an answer.
  3. Returning both the generated answer AND the source chunks used,
     so the UI can display page-level citations.

NOTE ON DESIGN: this is built as a small, explicit pipeline (retrieve ->
format -> prompt -> generate) rather than LangChain's older `RetrievalQA`
chain (from `langchain.chains`). LangChain has restructured its package
layout across versions (chains, prompts, and document loaders have moved
between `langchain`, `langchain_core`, and standalone packages several
times), which makes `langchain.chains` an unreliable import across
installed versions. Doing retrieval and prompting explicitly here uses
only `langchain_core` (stable) and `langchain_ollama`, avoiding that
churn entirely while doing exactly the same job.
"""

from dataclasses import dataclass
from typing import List

from langchain_ollama import OllamaLLM

try:
    # Modern, stable location for PromptTemplate
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate

from . import config


@dataclass
class QAPipeline:
    """Bundles the pieces needed to answer a question: retriever, LLM, prompt."""
    retriever: object
    llm: OllamaLLM
    prompt: PromptTemplate


def get_llm() -> OllamaLLM:
    """
    Connect to the local Ollama server and load Llama 3.2:3B.

    Requires Ollama to be installed and running locally, and the model
    pulled beforehand via:  `ollama pull llama3.2:3b`
    """
    return OllamaLLM(
        model=config.OLLAMA_MODEL,
        base_url=config.OLLAMA_BASE_URL,
        temperature=config.LLM_TEMPERATURE,
    )


def build_qa_chain(retriever) -> QAPipeline:
    """
    Build the end-to-end RAG pipeline:
        question -> retriever finds top-k relevant chunks
                 -> chunks + question are formatted into the prompt
                 -> Llama 3.2:3B generates a grounded answer
    """
    llm = get_llm()
    prompt = PromptTemplate(
        template=config.QA_PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )
    return QAPipeline(retriever=retriever, llm=llm, prompt=prompt)


def _retrieve_docs(retriever, question: str) -> List:
    """
    Fetch relevant chunks from the retriever, compatible with both
    newer (`.invoke`) and older (`.get_relevant_documents`) LangChain
    retriever interfaces.
    """
    if hasattr(retriever, "invoke"):
        return retriever.invoke(question)
    return retriever.get_relevant_documents(question)


def answer_question(qa_chain: QAPipeline, question: str) -> dict:
    """
    Run a question through the RAG pipeline.

    Returns a dict with:
        - answer: the generated text answer
        - sources: list of {content, source, page} for each retrieved chunk
    """
    docs = _retrieve_docs(qa_chain.retriever, question)

    # "Stuff" all retrieved chunks into a single context block, separated
    # for readability -- this mirrors LangChain's "stuff" chain strategy.
    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    formatted_prompt = qa_chain.prompt.format(context=context, question=question)
    answer_text = qa_chain.llm.invoke(formatted_prompt)

    sources = [
        {
            "content": doc.page_content,
            "source": doc.metadata.get("source", "unknown"),
            "page": doc.metadata.get("page", "unknown"),
        }
        for doc in docs
    ]

    return {
        "answer": str(answer_text).strip(),
        "sources": sources,
    }