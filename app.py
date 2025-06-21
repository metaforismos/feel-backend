from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from PIL import Image
import io
import torch
from transformers import pipeline

app = FastAPI()
emotion_model = pipeline("image-classification", model="nateraw/ferplus")

@app.post("/detect-emotions/")
async def detect_emotions(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        try:
            preds = emotion_model(image)
            top_emotion = sorted(preds, key=lambda x: x["score"], reverse=True)[0]
            results.append({
                "filename": file.filename,
                "emotion": top_emotion["label"],
                "confidence": round(top_emotion["score"], 2)
            })
        except Exception as e:
            results.append({"filename": file.filename, "error": str(e)})
    return JSONResponse(content={"results": results})
