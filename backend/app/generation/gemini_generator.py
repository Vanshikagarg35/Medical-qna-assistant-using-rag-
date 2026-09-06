import httpx
from app.config import settings

def generate_with_gemini(question, contexts, mode):
    evidence = "\n\n".join(
        f"[{i+1}] {c['title']} | {c.get('section', 'General')}\n{c['text']}"
        for i, c in enumerate(contexts)
    )
    prompt = (
        "You are MedSamjho, an educational medical information assistant. "
        "Answer ONLY from the evidence.\n"
        "Rules: Do not diagnose. Do not prescribe. Do not give personalized dosage. "
        "Do not add unsupported facts. Cite factual statements using only [1], [2], etc. "
        "If evidence is insufficient, respond exactly INSUFFICIENT_EVIDENCE. "
        f"Use patient-friendly language. Mode: {mode}.\n"
        f"Question: {question}\nEvidence:\n{evidence}"
    )
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{settings.gemini_model}:generateContent?key={settings.gemini_api_key}"
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.1, "maxOutputTokens": 700},
    }
    response = httpx.post(url, json=payload, timeout=45)
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
