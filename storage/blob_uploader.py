
from azure.storage.blob import BlobServiceClient
import os
import uuid

def upload_to_blob(file_bytes: bytes, filename: str) -> str:
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = "legal-documents"

    blob_service = BlobServiceClient.from_connection_string(conn_str)
    container_client = blob_service.get_container_client(container_name)

    # create container if not exists
    try:
        container_client.create_container()
    except Exception:
        pass

    blob_name = f"{uuid.uuid4()}-{filename}"
    blob_client = container_client.get_blob_client(blob_name)

    blob_client.upload_blob(file_bytes, overwrite=True)

    return blob_name
