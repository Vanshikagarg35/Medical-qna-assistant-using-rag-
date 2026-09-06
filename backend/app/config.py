from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict
ROOT=Path(__file__).resolve().parents[2]
LOCAL_EMBEDDING_MODEL=ROOT/'models'/'all-MiniLM-L6-v2'
class Settings(BaseSettings):
 frontend_origin:str='http://localhost:5173'
 embedding_model:str=str(LOCAL_EMBEDDING_MODEL if LOCAL_EMBEDDING_MODEL.exists() else 'sentence-transformers/all-MiniLM-L6-v2')
 top_k:int=4
 min_score:float=.32
 llm_provider:str='extractive'
 gemini_api_key:str=''
 gemini_model:str='gemini-2.5-flash'
 model_config=SettingsConfigDict(env_file=ROOT/'.env',extra='ignore')
settings=Settings()
