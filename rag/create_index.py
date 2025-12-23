import os
from dotenv import load_dotenv
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField
)
from azure.core.credentials import AzureKeyCredential

load_dotenv()

index_name = os.getenv("AZURE_SEARCH_INDEX")

index_client = SearchIndexClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

fields = [
    SimpleField(name="id", type="Edm.String", key=True),
    SearchableField(name="text", type="Edm.String"),
    SimpleField(name="source", type="Edm.String")
]

index = SearchIndex(name=index_name, fields=fields)

# Create index
index_client.create_or_update_index(index)

print("INDEX CREATED SUCCESSFULLY")
