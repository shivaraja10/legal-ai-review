from rag.index_documents import index_text

def ingest_document(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    index_text(text, path)
    return "Document indexed successfully"
