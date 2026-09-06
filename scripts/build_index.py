from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'backend'))
from app.ingestion.loader import load_processed_folder
from app.retrieval.faiss_retriever import retriever
records=load_processed_folder(ROOT/'data/processed');retriever.build(records);print(f'Built FAISS index with {len(records)} chunks')
