from legal_kernel.azure_openai import chat
from rag.retrieve_context import retrieve_context


def validate_clause(clause: str):
    context = retrieve_context(clause)

    prompt = f"""
Validate the clause against regulations below.
If non-compliant:
- Explain why
- Cite regulation
- Risk level

Clause:
{clause}

Regulations:
{context}
"""
    return chat(prompt)
