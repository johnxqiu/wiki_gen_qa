"""Simple RAG implementation for Wikipedia QA."""
import os
from typing import List

from langchain import hub
from langchain.embeddings.sentence_transformer import \
    SentenceTransformerEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import vectorstores
from langchain_core.language_models.chat_models import BaseChatModel

os.environ["TOKENIZERS_PARALLELISM"] = "false"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def format_docs(in_docs) -> str:
    return "\n\n".join(doc.page_content for doc in in_docs)


class SimpleRAG:
    def __init__(
        self,
        in_content: str,
        in_chat: BaseChatModel,
        in_chunk_size: int = 400,
        in_chunk_overlap: int = 0,
    ):
        self.llm = in_chat
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=in_chunk_size, chunk_overlap=in_chunk_overlap
        )
        self.embedding = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)
        split_content = self.text_splitter.split_text(in_content)
        self.db = vectorstores.Chroma.from_texts(split_content, self.embedding)
        self.retriever = self.db.as_retriever()
        self.rag_prompt = hub.pull("rlm/rag-prompt")
        self.rag_chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | self.rag_prompt
            | self.llm
            | StrOutputParser()
        )
