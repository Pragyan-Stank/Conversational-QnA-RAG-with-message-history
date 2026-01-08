from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
# Persistence
VECTOR_DIR: str = str(Path.home() / '.rag_vectors')


# Embeddings
EMBEDDING_MODEL: str = 'sentence-transformers/all-MiniLM-L6-v2'


# LLM (llama/groq/openai etc) -- keep as string and instantiate elsewhere
LLM_MODEL: str = 'gpt-4o-mini' # replace with real model


# Chunking
CHUNK_SIZE: int = 1000
CHUNK_OVERLAP: int = 200


# Retriever
TOP_K: int = 5


# Environment
DEBUG: bool = True


class Config:
env_file = '.env'


settings = Settings()
