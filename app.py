# app.py
from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from ingestion import ingest_pdf
from rag_chain import conversational_rag

app = FastAPI(title="Conversational PDF RAG Chatbot")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ingest_pdf(file_path)

    return {"message": "PDF ingested successfully"}

@app.post("/chat/")
async def chat(
    session_id: str = Form(...),
    question: str = Form(...)
):
    response = conversational_rag.invoke(
        {"input": question},
        config={"configurable": {"session_id": session_id}}
    )

    return {"answer": response["answer"]}
