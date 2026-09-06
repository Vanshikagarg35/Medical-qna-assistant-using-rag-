import re
EMERGENCY=[r'severe chest pain',r'difficulty breathing',r'cannot breathe',r'gasping',r'unconscious',r'not responding',r'heavy bleeding',r'stroke',r'overdose',r'poison',r'seizure',r'saans.*nahi',r'behosh']
INJECTION=[r'ignore .*previous instructions',r'reveal .*system prompt',r'bypass .*safety',r'developer message']
PRESCRIPTION=[r'exact dosage',r'prescribe',r'which medicine should i take',r'dawai batao',r'kitni dose']
PII=[r'\b\d{12}\b',r'\b[A-Z]{5}\d{4}[A-Z]\b',r'\b[6-9]\d{9}\b']
def hit(text,patterns):return any(re.search(p,text.lower()) for p in patterns)
def assess_input(text):
 return {'emergency':hit(text,EMERGENCY),'injection':hit(text,INJECTION),'prescription':hit(text,PRESCRIPTION),'pii':hit(text,PII)}
