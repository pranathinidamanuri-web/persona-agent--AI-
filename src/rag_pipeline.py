import os

documents = {}

def load_documents():
    for file in os.listdir("data"):
        path = os.path.join("data", file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                documents[file] = f.read()
        except:
            continue  # skip pdf or unreadable


def score(text, query):
    text = text.lower()
    query_words = query.lower().split()

    # remove common useless words
    stopwords = ["is", "the", "an", "a", "it", "been", "this", "that"]

    meaningful_words = [w for w in query_words if w not in stopwords]

    match_count = sum(1 for word in meaningful_words if word in text)

    return match_count


def retrieve(query, top_k=2):
    if not documents:
        return "", []

    scored_docs = []

    for file, text in documents.items():
        s = score(text, query)

        # IMPORTANT FILTER
        if s >= 2:
            scored_docs.append((s, file, text))

    # sort by best match
    scored_docs.sort(reverse=True)

    if not scored_docs:
        return "", []

    top_docs = scored_docs[:top_k]

    context = "\n\n".join([doc for _, _, doc in top_docs])
    sources = [file for _, file, _ in top_docs]

    return context, sources