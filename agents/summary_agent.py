from legal_kernel.azure_openai import chat


def generate_summary(findings: str):
    prompt = f"""
Summarize compliance findings for executives.
Include:
- Overall risk
- Key violations
- Recommendations

Findings:
{findings}
"""
    return chat(prompt)
