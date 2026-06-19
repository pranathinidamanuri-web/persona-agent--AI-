def generate_response(persona, context, query):

    if not context:
        return "No relevant information found."

    if persona == "Frustrated User":
        return f"I understand your frustration. Let's resolve this quickly.\n\n{context}"

    elif persona == "Technical Expert":
        return f"Technical details and resolution steps:\n\n{context}"

    else:  # Business Executive
        return f"This issue may impact operations. Summary below:\n\n{context}"