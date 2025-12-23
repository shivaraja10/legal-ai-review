from legal_kernel.azure_openai import chat


def extract_clauses(text: str):
    prompt = f"""
Extract legal clauses from the document.
Return JSON with:
- clause_type
- clause_text

Document:
{text}
"""
    return chat(prompt)
