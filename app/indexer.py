from langchain.vectorstores import Chroma
from langchain.schema import Document
from .embeddings import get_embeddings
from .config import settings
from .logger import logger
from typing import List




def create_or_load_db(docs: List[Document], persist: bool = True, collection_name: str = 'default'):
emb = get_embeddings()
persist_dir = settings.VECTOR_DIR
logger.info('Creating/loading Chroma at %s', persist_dir)
db = Chroma.from_documents(docs, embedding=emb, persist_directory=persist_dir, collection_name=collection_name)
if persist:
try:
db.persist()
except Exception as e:
logger.warning('Chroma persist failed: %s', e)
return db




def load_db(persist_dir: str = None, collection_name: str = 'default'):
emb = get_embeddings()
persist_dir = persist_dir or settings.VECTOR_DIR
return Chroma(persist_directory=persist_dir, embedding_function=emb, collection_name=collection_name)
