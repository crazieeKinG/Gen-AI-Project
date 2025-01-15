from app.core.services.logger.main import logger

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def document_splitter(documents: list[Document]):
    """
    Function to split the document into chunks

    Parameters:
    - documents: list[Document]
    """

    logger.info("=== Splitting PDF file into chunks ===")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=10)
    splitted_texts = text_splitter.split_documents(documents)

    logger.info("=== PDF file split into %d chunks ===", len(splitted_texts))

    return splitted_texts


def load_pdf_file(file_path: str):
    """
    Function to load a PDF file

    Parameters:
    - file_path: str
    """
    logger.info("=== Loading PDF file: %s ===", file_path)

    pdf_loader = PyPDFLoader(file_path)
    documents = pdf_loader.load()

    logger.info("=== PDF file loaded successfully: %s ===", file_path)

    return document_splitter(documents)
