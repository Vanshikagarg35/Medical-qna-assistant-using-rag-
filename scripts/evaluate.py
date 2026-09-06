from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'backend'))
from app.retrieval.faiss_retriever import retriever
from app.services.rag_pipeline import run_pipeline
retriever.load();cases=json.loads((ROOT/'data/evaluation/test_cases.json').read_text());results=[]
for c in cases:
 start=time.perf_counter();r=run_pipeline(c['question'],'simple');actual='emergency' if r['emergency'] else ('refuse' if r['refused'] else 'answer');results.append({**c,'actual':actual,'passed':actual==c['expected'],'latency_ms':round((time.perf_counter()-start)*1000,2)})
report={'total':len(results),'passed':sum(x['passed'] for x in results),'behavior_accuracy':round(sum(x['passed'] for x in results)/len(results),3),'results':results};(ROOT/'data/evaluation/latest_results.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
