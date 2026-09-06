# Learn the Code

- `ingestion/loader.py`: cleans PDFs and creates overlapping chunks.
- `retrieval/faiss_retriever.py`: converts chunks and questions into 384-dimensional MiniLM vectors and searches them with FAISS.
- `safety/input_guardrails.py`: blocks emergency, injection, identifier, and prescription-risk input.
- `services/query_normalizer.py`: replaces common Hinglish medical phrases.
- `services/rag_pipeline.py`: coordinates safety, retrieval, threshold, generation, and final response.
- `generation/gemini_generator.py`: sends only retrieved evidence to Gemini.
- `generation/citation_validator.py`: rejects citation numbers that do not correspond to retrieved sources.
- `safety/output_guardrails.py`: blocks basic diagnostic certainty and dosage patterns.

Viva summary: RAG equals Retrieval plus Augmented context plus Generation. Safe RAG adds safety checks before retrieval and validation after generation.
