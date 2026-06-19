def classify_persona(text):
    text = text.lower()

    # Frustrated User (strong + meaningful phrases)
    frustrated_keywords = [
        "not working", "nothing is working", "frustrated",
        "angry", "annoying", "issue", "problem",
        "stuck", "been an hour", "immediately",
        "demand", "refund", "bad experience"
    ]

    if any(word in text for word in frustrated_keywords):
        return "Frustrated User"

    # Technical Expert
    technical_keywords = [
        "api", "error", "database", "integration",
        "log", "exception", "stack trace",
        "auth", "token", "failure"
    ]

    if any(word in text for word in technical_keywords):
        return "Technical Expert"

    # Business Executive (default)
    return "Business Executive"