"""Minimal standalone speech-to-text demo server for NurseSync AI.

No database, no other project files needed. Just:
    pip install -r requirements.txt
    uvicorn server:app --reload

Then open index.html/patient.html (e.g. via VS Code Live Server) and
click Record.
"""

import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NurseSync Speech-to-Text Demo")

# Dev/demo only: the HTML page is opened from a different origin
# (Live Server / file://), so allow everything.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path(__file__).parent / "recordings"
UPLOAD_DIR.mkdir(exist_ok=True)

_model = None


def get_model():
    """Load the Whisper model once and cache it. Runs fully locally on
    CPU via faster-whisper — no API key, no per-request cost, and after
    the model is downloaded once, no internet needed either. Whisper is
    inherently multilingual (~99 languages, including Hindi, Punjabi,
    Tamil, Telugu, Bengali, etc.) with no extra setup required.
    """
    global _model
    if _model is None:
        from faster_whisper import WhisperModel

        _model = WhisperModel("base", device="cpu", compute_type="int8")
    return _model


@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...), language: Optional[str] = Form(None)):
    """Transcribe an uploaded audio clip.

    `language` is an optional ISO-639-1 code (e.g. "en", "hi", "pa").
    Leave it unset/empty to let Whisper auto-detect the spoken language.
    """
    dest = UPLOAD_DIR / f"{uuid.uuid4()}_{audio.filename or 'clip.webm'}"
    dest.write_bytes(await audio.read())

    try:
        model = get_model()
        segments, info = model.transcribe(
            str(dest),
            beam_size=5,
            language=language or None,
        )
        transcript = " ".join(segment.text.strip() for segment in segments).strip()
    except Exception as exc:  # pragma: no cover - surfaced to the demo UI
        raise HTTPException(status_code=500, detail=f"Transcription failed: {exc}") from exc

    return {
        "transcript": transcript or "(no speech detected)",
        "detected_language": info.language,
        "language_probability": round(info.language_probability, 3),
    }


@app.get("/")
def root():
    return {"status": "ok", "message": "Speech-to-text demo server is running"}
