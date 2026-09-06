# MedSamjho: Medical Q&A Assistant Using Safe RAG

## What proves the project claim

1. Medical texts are cleaned and chunked.
2. `all-MiniLM-L6-v2` creates dense embeddings.
3. FAISS retrieves the most relevant chunks.
4. Input guardrails intercept emergency, injection, PII, and prescription requests.
5. An evidence threshold refuses weak retrieval.
6. Gemini generates an answer only from retrieved evidence.
7. Citation numbers and generated output are validated.
8. An extractive fallback keeps the project usable without the API.

## Windows setup

Install Python 3.11 and Node.js LTS. Run `setup_windows.bat` once. Edit `.env` and paste a free Google AI Studio Gemini API key. Run `start_project.bat`. Frontend: `http://localhost:5173`. API docs: `http://localhost:8000/docs`.

The first index build downloads the free MiniLM embedding model and needs internet. Never commit `.env` or enter personal medical information. The included 20-topic corpus is synthetic starter content for software demonstration. Replace or expand it using approved official medical content before claiming real-source coverage.
