# Conversational PDF QnA RAG Chatbot

A production-oriented **Conversational Retrieval-Augmented Generation (RAG)** system built with **FastAPI**, designed to handle **large PDFs efficiently** while maintaining **multi-turn conversational context**.

This system enables users to upload PDFs and interact with them via a chat interface, supporting context-aware follow-up questions without reloading or re-embedding documents.

---

## 🚀 Key Features

- Conversational PDF Question-Answering
- Efficient handling of large PDFs (hundreds of pages)
- Persistent vector storage (no repeated embeddings)
- Session-based chat memory
- Query-rewriting for context-aware retrieval
- FastAPI-based deployment
- Minimal yet professional codebase structure

---

## 🧠 System Architecture

The system is divided into **two logical stages**, following industry RAG best practices:

### 1. Ingestion Pipeline
Responsible for:
- Loading PDF files
- Chunking content intelligently
- Generating embeddings
- Persisting vectors to disk

### 2. Conversational RAG Pipeline
Responsible for:
- Query contextualization using chat history
- Semantic retrieval from vector store
- Answer generation using retrieved context
- Managing multi-session chat memory


---

## 🔄 End-to-End Workflow

### Step 1: PDF Upload
- User uploads a PDF via API
- PDF is loaded page-by-page
- Text is recursively chunked
- Each chunk is embedded and stored persistently

### Step 2: Vector Persistence
- Embeddings are saved to disk using Chroma
- PDFs are embedded **only once**
- System is restart-safe

### Step 3: Conversational Querying
- User submits a question with a session ID
- Chat history is used to rewrite the query
- Only the most relevant chunks are retrieved
- LLM generates a concise answer

---

## 🧩 How Large PDFs Are Handled

- PDFs are split into small, semantically meaningful chunks
- Only top-K relevant chunks are retrieved per query
- Prompt size remains constant regardless of PDF size
- LLM never receives the full document
- Retrieval time is independent of document length

---

## 🧠 Conversational Memory Design

- Each session maintains isolated chat history
- Follow-up questions are rewritten into standalone queries
- Prevents prompt bloating
- Maintains retrieval accuracy across turns

---

## 🛠️ Setup Instructions

### 1. Clone Repository
```bash
git clone <repo-url>
cd rag_pdf_chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Server will start at:
```
http://localhost:8000
```

---

## 📤 API Usage

### Upload PDF
```
POST /upload-pdf/
```

### Chat with PDF
```
POST /chat/

Form Data:
- session_id: unique_session_identifier
- question: user_query
```

---

## 📈 Why This Is Production-Relevant

- Stateless API design
- Persistent vector storage
- Bounded LLM context
- Modular, extensible code
- Ready for containerization and scaling


This project focuses on **real-world RAG constraints**, prioritizing scalability, reliability, and clarity over experimental complexity.
