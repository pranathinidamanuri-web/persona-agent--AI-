import streamlit as st
import json

from src.classifier import classify_persona
from src.rag_pipeline import load_documents, retrieve
from src.generator import generate_response
from src.escalator import should_escalate, generate_handoff

# Title
st.title("Persona-Aware Support Agent")

# Load documents only once
if "loaded" not in st.session_state:
    load_documents()
    st.session_state.loaded = True

# User input
query = st.text_input("Enter your issue:")

if query:
    # Step 1: Persona Detection
    persona = classify_persona(query)

    # Step 2: Retrieval
    context, sources = retrieve(query)

    # Step 3: Escalation Check
    escalate = should_escalate(context, query)

    # Display Persona
    st.subheader("Detected Persona")
    st.write(persona)

    # Display Sources
    st.subheader("Retrieved Sources")
    if sources:
        for s in sources:
            st.write("-", s)
    else:
        st.write("No relevant sources found")

    # Step 4: Handle Escalation or Response
    if escalate:
        st.subheader("⚠️ Escalation Triggered")

        handoff = generate_handoff(persona, query, sources)

        # Show clean JSON
        try:
            st.json(json.loads(handoff))
        except:
            st.write(handoff)

    else:
        # Generate response
        response = generate_response(persona, context, query)

        st.subheader("Response")
        st.write(response)