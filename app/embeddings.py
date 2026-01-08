from typing import Iterable, List
from .config import settings
from langchain.embeddings import HuggingFaceEmbeddings




def get_embeddings():
return HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)




def embed_batch(texts: Iterable[str], batch_size: int = 32) -> List[List[float]]:
emb = get_embeddings()
texts = list(texts)
out = []
for i in range(0, len(texts), batch_size):
chunk = texts[i:i+batch_size]
out.extend(emb.embed_documents(chunk))
return out
