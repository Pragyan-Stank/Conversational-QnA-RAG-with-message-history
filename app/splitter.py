from langchain_text_splitters import RecursiveCharacterTextSplitter
from .config import settings
from typing import List
from langchain.schema import Document




def chunk_documents(docs: List[Document]) -> List[Document]:
splitter = RecursiveCharacterTextSplitter(
chunk_size=settings.CHUNK_SIZE,
chunk_overlap=settings.CHUNK_OVERLAP,
separators=["\n\n", "\n", " "]
)
return splitter.split_documents(docs)
