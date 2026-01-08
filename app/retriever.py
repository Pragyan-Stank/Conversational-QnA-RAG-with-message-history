from .indexer import load_db
from .config import settings
from .logger import logger




def get_retriever(top_k: int = None):
db = load_db()
top_k = top_k or settings.TOP_K
retriever = db.as_retriever(search_kwargs={'k': top_k})
logger.info('Retriever ready with top_k=%d', top_k)
return retriever
