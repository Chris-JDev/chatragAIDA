import re

AIDA_KEYWORDS = {
    "Awareness": ["introducing", "discover", "did you know", "brand new", "launch", "attention", "aware", "just dropped"],
    "Interest": ["features", "benefits", "learn more", "why", "curious", "details", "functionality", "how it works"],
    "Desire": ["imagine", "you deserve", "loved by", "trusted by", "join the community", "feel", "experience", "aspire"],
    "Action": ["buy now", "click here", "subscribe", "order today", "limited offer", "sign up", "act now", "don't miss out"]
}

def classify_aida_stage(text: str) -> str:
    text_lower = text.lower()
    scores = {stage: 0 for stage in AIDA_KEYWORDS}
    for stage, keys in AIDA_KEYWORDS.items():
        for kw in keys:
            if re.search(rf"\b{re.escape(kw)}\b", text_lower):
                scores[stage] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "Unclassified"
