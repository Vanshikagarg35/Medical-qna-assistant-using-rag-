PHRASES={'sugar badhne':'high blood glucose','sugar high':'high blood glucose','kya symptoms':'what symptoms','kya hota hai':'what is','bp':'blood pressure','bukhar':'fever','khansi':'cough','saans':'breathing','chakkar':'dizziness','sir dard':'headache','pet dard':'abdominal pain','kaise bache':'how to prevent','ilaaj':'treatment information','jalan':'burning sensation'}
def normalize_query(question):
 q=' '+question.lower().strip()+' '
 for source,target in PHRASES.items():q=q.replace(source,target)
 return ' '.join(q.split()).capitalize()
