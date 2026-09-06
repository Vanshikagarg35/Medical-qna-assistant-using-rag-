from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import ChatRequest
from app.services.rag_pipeline import run_pipeline
from app.retrieval.faiss_retriever import retriever
@asynccontextmanager
async def lifespan(app):retriever.load();yield
app=FastAPI(title='MedSamjho Safe RAG',version='2.0.0',description='Medical Q&A using safety-aware retrieval-augmented generation',lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=[settings.frontend_origin],allow_methods=['*'],allow_headers=['*'])
@app.get('/health')
def health():return {'status':'ok','indexed_chunks':len(retriever.records),'llm_provider':settings.llm_provider}
@app.post('/api/v1/chat')
def chat(request:ChatRequest):return run_pipeline(request.question,request.mode)
