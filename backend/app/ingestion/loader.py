import json,re
from pathlib import Path
import fitz

def clean_text(text):return re.sub(r'\s+',' ',text).strip()
def chunk_text(text,size=700,overlap=100):
 text=clean_text(text);out=[];start=0
 while start<len(text):
  end=min(len(text),start+size);part=text[start:end]
  if end<len(text):
   cut=part.rfind('. ')
   if cut>size//2:end=start+cut+1;part=text[start:end]
  if len(part)>=100:out.append(part)
  if end>=len(text):break
  start=max(start+1,end-overlap)
 return out
def load_json(path):
 data=json.loads(Path(path).read_text(encoding='utf-8'));return data if isinstance(data,list) else data.get('records',[])
def load_pdf(path,metadata):
 records=[]
 with fitz.open(path) as doc:
  for page_no,page in enumerate(doc,1):
   for idx,text in enumerate(chunk_text(page.get_text()),1):records.append({**metadata,'chunk_id':f"{metadata['source_id']}_p{page_no}_c{idx}",'page':page_no,'text':text})
 return records
def load_processed_folder(folder):
 records=[]
 for path in Path(folder).glob('*.json'):
  try:records.extend(x for x in load_json(path) if x.get('text'))
  except Exception:pass
 unique={}
 for r in records:unique[(r.get('title'),r.get('section'),r.get('text'))]=r
 return list(unique.values())
