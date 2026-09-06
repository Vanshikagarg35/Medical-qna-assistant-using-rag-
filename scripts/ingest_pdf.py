from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'backend'))
from app.ingestion.loader import load_pdf
if len(sys.argv)<6:raise SystemExit('Usage: python scripts/ingest_pdf.py file.pdf SOURCE_ID TITLE ORGANIZATION URL')
meta={'source_id':sys.argv[2],'title':sys.argv[3],'organization':sys.argv[4],'url':sys.argv[5],'section':'Document'};records=load_pdf(sys.argv[1],meta)
out=ROOT/f'data/processed/{sys.argv[2]}_chunks.json';out.write_text(json.dumps(records,indent=2));print('Saved',len(records),'chunks')
