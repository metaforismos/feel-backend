# Feel – Emotion Recognition Backend

This backend service receives one or more image files and returns the dominant emotion detected in each image using a pre-trained model (`nateraw/ferplus` from Hugging Face).

## Features

- Upload multiple images
- Detects primary emotion per photo
- Returns label and confidence score
- Built with FastAPI

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
