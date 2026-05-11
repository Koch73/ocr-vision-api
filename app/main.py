from fastapi import FastAPI, UploadFile, File, HTTPException
from app.ocr import extract_text
from app.ai.ai_summary import summarize_text

import shutil
import uuid
import os

app = FastAPI()

UPLOAD_DIR = "/tmp"


@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}.jpg"

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save uploaded file: {str(e)}")

    try:
        response = extract_text(file_path)
        print(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    return {
        "response": response
    }

@app.post("/summarize")
async def summarize_endpoint(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}.jpg"

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save uploaded file: {str(e)}")

    try:
        ocr_result = extract_text(file_path)
        extracted_text = ocr_result.get("text", "")
        summary = summarize_text(extracted_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing summary: {str(e)}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    return {
        "summary": summary,
        "text": extracted_text
    }

