# Persona-Aware Customer Support Agent

## 📌 Project Overview

This project is an AI-powered customer support agent that dynamically adapts its responses based on the user's persona.

The system detects the user's intent and tone, retrieves relevant information from a knowledge base using a Retrieval-Augmented Generation (RAG) pipeline, and generates responses accordingly. It also escalates issues to a human agent when necessary.

---

## ⚙️ Tech Stack

* Python 3.11+
* Streamlit (UI)
* Sentence Transformers (Embeddings - optional fallback)
* Custom keyword-based classifier
* Local document-based RAG (no external vector DB)

---

## 🏗️ Architecture

User Query
→ Persona Detection
→ Document Retrieval (RAG)
→ Escalation Check
→ Response Generation OR Human Handoff

---

## 🧠 Persona Detection Strategy

We use a rule-based classifier with keyword matching:

* **Frustrated User** → emotional words (e.g., "not working", "frustrated", "refund")
* **Technical Expert** → technical terms (e.g., "API", "error", "logs")
* **Business Executive** → default fallback

---

## 📚 RAG Pipeline Design

* Documents stored in `/data`
* Loaded into memory
* Query-based keyword scoring
* Top-K retrieval (TOP_K = 2)
* Low-relevance queries trigger escalation

---

## 🚨 Escalation Logic

Escalation is triggered when:

* No relevant documents found
* Query contains sensitive terms (refund, billing, payment)
* Confidence is low

---

## 🧾 Human Handoff Format

```json
{
  "persona": "Frustrated User",
  "issue": "Nothing is working",
  "documents_used": [],
  "recommended_action": "Human intervention required"
}
```

---

## ▶️ Setup Instructions

```bash
git clone <your-repo-link>
cd persona-agent
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Variables

If using LLM APIs:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 🧪 Example Queries

1. Nothing is working
2. API authentication error
3. I want a refund immediately
4. Forgot my password
5. How does this impact operations?

---

## ⚠️ Known Limitations

* Basic keyword-based persona detection
* No advanced embeddings (optional improvement)
* Limited document understanding
* No multi-turn conversation memory

---

## 🚀 Future Improvements

* Add vector DB (Chroma / FAISS)
* Improve classification using LLM
* Add chat history memory
* Add confidence scoring
* Deploy as API

---
