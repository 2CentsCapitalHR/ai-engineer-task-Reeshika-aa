# ADGM Corporate Agent - RAG with Groq

This repository contains a simple RAG pipeline using the Groq API (preferred) with a fallback to SentenceTransformers embeddings. It parses uploaded .docx files and the provided Task.pdf resources, builds a FAISS vectorstore, and serves a small Gradio UI to query the corpus using Groq as the LLM.

Quick steps:
1. Create a Python venv and install dependencies: `pip install -r requirements.txt`
2. Set `GROQ_API_KEY` environment variable if you want to use Groq embeddings + Groq chat. If not set, the pipeline falls back to local sentence-transformers embeddings.
3. Place example files in `uploads/` (there is often a sample `Task.pdf` available in `/mnt/data/Task.pdf` in some environments).
4. Run `python gradio_app.py` and open the Gradio URL.

Notes:
- The code uses an OpenAI-compatible Groq endpoint. If your Groq account uses a different endpoint, update `GROQ_EMBEDDING_ENDPOINT` in `embeddings.py` and `GROQ_CHAT_ENDPOINT` in `rag.py`.
- The embedding model string is configurable.
