import pickle
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import settings
ROOT=Path(__file__).resolve().parents[3];STORE=ROOT/'vector_store';INDEX=STORE/'medical.faiss';META=STORE/'metadata.pkl'
class FaissRetriever:
 def __init__(self):self.model=None;self.index=None;self.records=[]
 def get_model(self):
  if self.model is None:self.model=SentenceTransformer(settings.embedding_model,local_files_only=True)
  return self.model
 def build(self,records):
  vectors=self.get_model().encode([r['text'] for r in records],normalize_embeddings=True,show_progress_bar=True).astype('float32')
  self.index=faiss.IndexFlatIP(vectors.shape[1]);self.index.add(vectors);self.records=records
  STORE.mkdir(parents=True,exist_ok=True);faiss.write_index(self.index,str(INDEX));pickle.dump(records,open(META,'wb'))
 def load(self):
  if not INDEX.exists() or not META.exists():return False
  self.index=faiss.read_index(str(INDEX));self.records=pickle.load(open(META,'rb'));return True
 def search(self,query,k=None):
  if self.index is None:return []
  k=min(k or settings.top_k,len(self.records));q=self.get_model().encode([query],normalize_embeddings=True).astype('float32');scores,ids=self.index.search(q,k)
  return [{**self.records[int(i)],'score':round(float(s),4)} for s,i in zip(scores[0],ids[0]) if i>=0]
retriever=FaissRetriever()
