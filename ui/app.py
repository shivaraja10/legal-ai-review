import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from legal_kernel.planner import run_pipeline




st.title("AI Legal Document Review Assistant")

file = st.file_uploader("Upload document")
if file:
    path = f"data/contracts/{file.name}"
    with open(path, "wb") as f:
        f.write(file.getvalue())
    if st.button("Analyze"):
        st.write(run_pipeline(path))
