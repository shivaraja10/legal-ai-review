import os
import re
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

def safe_id(value: str) -> str:
    """
    Azure Search keys allow only:
    letters, digits, _, -, =
    """
    value = value.replace("\\", "_").replace("/", "_")
    value = re.sub(r"[^A-Za-z0-9_\-=]", "_", value)
    return value

def index_text(text, source):
    doc = {
        "id": safe_id(source),   # ✅ FIXED
        "text": text,
        "source": source
    }
    client.upload_documents([doc])
