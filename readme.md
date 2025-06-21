# Feel – Emotion Recognition Backend (FER Version)

This backend service receives one or more image files and returns the dominant emotion detected using the open-source `fer` library.

## Features

- Upload multiple images
- Detects primary emotion per photo
- Returns label and confidence score
- Built with FastAPI

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
