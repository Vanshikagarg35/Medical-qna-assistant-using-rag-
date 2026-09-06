import re
def extractive_answer(contexts,mode):
 sentences=[]
 for c in contexts:sentences.extend(x.strip() for x in re.split(r'(?<=[.!?])\s+',c['text']) if len(x.strip())>30)
 limit=3 if mode=='simple' else 6
 prefix={'simple':'In simple words: ','detailed':'Evidence-based overview: ','safety':'Key safety information: '}[mode]
 return prefix+' '.join(sentences[:limit])
