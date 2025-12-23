from rag.index_documents import client

def retrieve_context(query, top_k=3):
    results = client.search(query, top=top_k)
    return "\n".join([r["text"] for r in results])
