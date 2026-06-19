import json

def should_escalate(context, query):
    if not context:
        return True

    sensitive_words = ["refund", "charge", "billing", "payment"]

    if any(word in query.lower() for word in sensitive_words):
        return True

    return False


def generate_handoff(persona, query, sources):
    data = {
        "persona": persona,
        "issue": query,
        "documents_used": sources,
        "recommended_action": "Human intervention required"
    }

    return json.dumps(data, indent=2)