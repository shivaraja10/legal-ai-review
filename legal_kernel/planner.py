from agents.ingestion_agent import ingest_document
from agents.clause_agent import extract_clauses
from agents.compliance_agent import validate_clause
from agents.summary_agent import generate_summary

def run_pipeline(doc_path):
    ingest_document(doc_path)
    text = open(doc_path).read()
    clauses = extract_clauses(text)
    findings = validate_clause(clauses)
    return generate_summary(findings)
