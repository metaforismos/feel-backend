from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from PIL import Image
import io
import cv2
import numpy as np
from fer import FER

app = FastAPI()
emotion_detector = FER(mtcnn=True)

@app.post("/detect-emotions/")
async def detect_emotions(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        contents = await file.read()
        np_img = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        try:
            emotions = emotion_detector.detect_emotions(img)
            if emotions and 'emotions' in emotions[0]:
                emotion_scores = emotions[0]["emotions"]
                top_emotion = max(emotion_scores, key=emotion_scores.get)
                confidence = round(emotion_scores[top_emotion], 2)
                results.append({
                    "filename": file.filename,
                    "emotion": top_emotion,
                    "confidence": confidence
                })
            else:
                results.append({"filename": file.filename, "emotion": "Unknown"})
        except Exception as e:
            results.append({"filename": file.filename, "error": str(e)})
    return JSONResponse(content={"results": results})
