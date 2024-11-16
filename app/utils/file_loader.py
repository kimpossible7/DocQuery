from fastapi import UploadFile
import json
from pdfminer.high_level import extract_text
import io

async def load_document(file: UploadFile) -> str:
    if file.content_type not in ["application/json", "application/pdf"]:
        raise ValueError("Unsupported file type. Only JSON and PDF are allowed.")
    
    content = ""
    if file.content_type == "application/json":
        content = await file.read()
        content = json.loads(content.decode())["content"]
    elif file.content_type == "application/pdf":
        content = extract_text(io.BytesIO(await file.read()))
    else:
        raise ValueError("Unsupported file type. Only JSON and PDF are allowed.")
    return content
