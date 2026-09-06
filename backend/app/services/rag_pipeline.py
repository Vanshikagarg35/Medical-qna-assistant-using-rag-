from app.config import settings
from app.safety.input_guardrails import assess_input
from app.safety.output_guardrails import is_safe_output
from app.services.query_normalizer import normalize_query
from app.retrieval.faiss_retriever import retriever
from app.generation.extractive_fallback import extractive_answer
from app.generation.gemini_generator import generate_with_gemini
from app.generation.citation_validator import citations_valid
DISCLAIMER='General educational information only. This application does not diagnose, prescribe treatment, or replace a qualified healthcare professional.'
def run_pipeline(question,mode):
 normalized=normalize_query(question);risk=assess_input(question);base={'normalized_question':normalized,'citations':[],'confidence':'low','emergency':False,'refused':False,'generator':'none','disclaimer':DISCLAIMER}
 if risk['emergency']:return {**base,'answer':'The symptoms mentioned may require urgent medical attention. Contact local emergency services or go to the nearest emergency department now. Do not rely only on this application.','emergency':True,'refused':True,'generator':'safety-rule'}
 if risk['injection']:return {**base,'answer':'I cannot follow instructions that attempt to bypass the application safety rules.','refused':True,'generator':'safety-rule'}
 if risk['pii']:return {**base,'answer':'Please remove personal identifiers such as phone, Aadhaar, PAN, or medical-record numbers, then ask again.','refused':True,'generator':'safety-rule'}
 if risk['prescription']:return {**base,'answer':'I cannot prescribe medicine or provide personalized dosage. I can provide general source-grounded educational information.','refused':True,'generator':'safety-rule'}
 results=retriever.search(normalized+' '+question,settings.top_k)
 if not results or results[0]['score']<settings.min_score:return {**base,'answer':'I could not find sufficient information in the approved medical knowledge base to answer reliably. Please consult a qualified healthcare professional.','refused':True,'generator':'evidence-rule'}
 contexts=[r for r in results if r['score']>=settings.min_score]
 answer=extractive_answer(contexts,mode);generator='extractive-fallback'
 if settings.llm_provider=='gemini' and settings.gemini_api_key:
  try:
   candidate=generate_with_gemini(question,contexts,mode)
   if candidate!='INSUFFICIENT_EVIDENCE' and citations_valid(candidate,len(contexts)) and is_safe_output(candidate):answer=candidate;generator='gemini-grounded'
  except Exception:pass
 if not is_safe_output(answer):return {**base,'answer':'The generated response did not pass the output safety check. Please consult a qualified healthcare professional.','refused':True,'generator':'output-safety'}
 citations=[{'id':i+1,'title':c['title'],'organization':c.get('organization',''),'section':c.get('section',''),'url':c.get('url',''),'page':c.get('page'),'score':c['score']} for i,c in enumerate(contexts)]
 return {**base,'answer':answer,'citations':citations,'confidence':'high' if contexts[0]['score']>=.60 else 'medium','generator':generator}
