from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io
from utils.detector import detect_image_type
from utils.routes import route_analysis

app = FastAPI()

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image_type = detect_image_type(image)
    result = route_analysis(image, image_type)

    return JSONResponse(content={"type": image_type, "result": result})