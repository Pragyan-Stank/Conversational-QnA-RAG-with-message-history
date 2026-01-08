from typing import List
from langchain.document_loaders import UnstructuredPDFLoader, TextLoader
from langchain.schema import Document
from .logger import logger




def load_pdf(path: str) -> List[Document]:
"""Load PDF using Unstructured loader (handles large PDFs streamingly)."""
logger.info('Loading PDF: %s', path)
loader = UnstructuredPDFLoader(path)
docs = loader.load()
logger.info('Loaded %d documents/pages', len(docs))
return docs




def load_text(path: str) -> List[Document]:
logger.info('Loading text: %s', path)
loader = TextLoader(path, encoding='utf-8')
return loader.load()
