# NurseSync AI

**Speak. Sync. Care.**

A voice-driven nurse shift handoff system. A nurse speaks the handoff out loud at the bedside, the audio is transcribed automatically on the server, and the transcript is returned for review and correction before it is saved.

Built for **UCS503P — Software Engineering Project**, Thapar Institute of Engineering & Technology, Patiala.

---

## The Problem

Shift handoff is the moment a patient is most likely to fall through the cracks. When one nurse hands a ward over to the next, the transfer happens verbally, under time pressure, at the end of a long shift. Nothing is written down until later, if at all.

The consequences are well documented: medication details get dropped, changes in a patient's condition are summarised away, and the incoming nurse inherits an incomplete picture. Communication failure during handoff is a recognised contributor to preventable in-hospital harm.

Both existing alternatives fail in practice. Free-text notes typed after the shift are rushed, inconsistent and written from memory. Structured digital forms are thorough but too slow to complete mid-shift, so nurses skip them entirely.

## The Approach

NurseSync AI removes the tradeoff by letting the nurse do the thing they already do — talk — and handling the capture automatically.

Transcription runs **locally on the server**. This is a deliberate architectural decision rather than a convenience: a handoff contains protected patient health information, and routing that audio to a third-party cloud API would create a privacy exposure no hospital could reasonably accept. Running the model on-premise keeps the audio inside the institution's own infrastructure — and as a consequence there is no API key, no per-request cost, and no dependency on connectivity once the model is cached.

The model is multilingual out of the box — English, Hindi, Punjabi, Tamil, Telugu and Bengali among roughly 99 supported languages — which matters in an Indian hospital where nursing staff do not all hand off in English.

---

## What Works Today

The speech-to-text pipeline runs end to end and is demonstrable.

| Capability | Status |
|---|---|
| Record audio in the browser (`MediaRecorder`) | Working |
| Upload to the backend as multipart form data | Working |
| Server-side transcription with faster-whisper | Working |
| Explicit language selection **or** automatic detection | Working |
| Live `Recording…` / `Transcribing…` state feedback | Working |
| Editable transcript for nurse review before saving | Working |
| Per-patient handoff history | Working (browser `localStorage`) |
| Readable error messages on backend failure | Working |
| Static UI screens — login, dashboard, patient list, patient detail | Working (demo only, no authentication) |

## What Is Designed But Not Yet Built

These are specified in the proposal, DFDs, ER diagram and activity diagram, but are **not** implemented in this repository.

| Component | Where it is specified |
|---|---|
| Database persistence (PostgreSQL, seven-entity schema) | ER diagram |
| Medical entity extraction (NLP) | Activity diagram, DFD Level 2 |
| Automatic SBAR summarisation | Activity diagram, `Handoff.SBARSummary` |
| Completeness scoring and missing-field flagging | Activity diagram, `Handoff.CompletenessScore` |
| Deterioration risk classification | ER diagram (`RiskAssessment`) |
| RAG-based AI assistant | Activity diagram |
| Authentication and role-based access | Proposal |

Handoffs currently persist to browser storage, not to a database.

> This is an academic prototype. It has not been clinically validated and is **not approved for use in patient care**.

---

## Tech Stack

**Backend** — Python, FastAPI, Uvicorn, python-multipart
**Speech recognition** — faster-whisper (`base` model), running locally on CPU with int8 quantisation
**Frontend** — HTML, CSS, vanilla JavaScript, browser `MediaRecorder` API
**Deployment** — GitHub Actions publishing to GitHub Pages

---

## Repository Structure

```
NurseSync/
├── .github/workflows/
│   └── deploy-demo.yml         Publishes the demo to GitHub Pages
├── assets/
├── code/
│   └── speech-to-text-demo/    The runnable prototype
│       ├── server.py           FastAPI app exposing POST /transcribe
│       ├── requirements.txt
│       ├── index.html          Entry page
│       ├── login.html
│       ├── dashboard.html
│       ├── patients.html       Patient list
│       ├── patient.html        Patient detail + record handoff
│       ├── styles.css
│       └── HOW_TO_RUN.txt
├── doc/
│   ├── NurseSync.pptx          Presentation deck
│   └── UML Diagrams/
│       ├── NurseSync_DFD.pdf
│       ├── ER_Diagram.drawio.pdf
│       ├── NurseSync_Activity_Diagram.pdf
│       ├── UML_NurseSync_UserCase.drawio-4.pdf
│       └── UML_NurseSync_UserCase.xml
├── proposal/
│   ├── NurseSync_Project_Proposal.pdf
│   └── main.tex                LaTeX source
├── journals/                   Weekly progress journals
├── project-report-prototype-stage/
├── project-report-final/
├── Makefile
└── README.md
```

---

## Running the Demo

The prototype is standalone — no database and no other part of the project is required.

### 1. Start the backend

```bash
cd code/speech-to-text-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app
```

Wait for `Application startup complete`. Confirm the server is live at `http://127.0.0.1:8000` — it should return `{"status": "ok", ...}`.

### 2. Open the page

Serve `index.html` through a local web server (VS Code's **Live Server** extension works) rather than double-clicking it.

**Microphone access requires a secure context.** Browsers only expose `getUserMedia` over HTTPS or on `localhost`, so opening the page as a `file://` URL blocks recording outright. For an HTTPS demo, generate a locally-trusted certificate with [mkcert](https://github.com/FiloSottile/mkcert).

### 3. Record a handoff

Open a patient, choose a language (or leave it on auto-detect), click **Record Handoff**, speak, then click **Stop**. The clip uploads, comes back transcribed, and appears in an editable field for review before saving.

### Two things that will otherwise cost you an hour

**The first transcription after a cold start takes 10–20 seconds** while the model loads into memory. Every request after that is fast, because the model is cached rather than reloaded.

**Do not run `uvicorn` with a bare `--reload`.** It watches the entire virtualenv, restarting the server continuously and discarding the loaded model each time. If you need it while editing:

```bash
uvicorn server:app --reload --reload-exclude '.venv/*'
```

---

## How It Works

```
Browser                          FastAPI server                  faster-whisper
───────                          ──────────────                  ──────────────
MediaRecorder captures audio
        │
        ├─ Blob (audio/webm)
        ├─ FormData: audio + language
        │
        └──── POST /transcribe ──────▶ save upload to disk
                                       (uuid-prefixed filename)
                                                │
                                                └──── model.transcribe() ──▶ segments + language info
                                                │
                                       join segment text
        ◀──── JSON response ───────────┘
        │
   editable <textarea>
        │
   nurse reviews and corrects
        │
   save to handoff history
```

The recognition model is loaded **once** into a module-level global and reused across requests. Loading it per request would add 10–20 seconds to every transcription.

---

## API Reference

### `POST /transcribe`

**Request** — `multipart/form-data`

| Field | Type | Required | Description |
|---|---|---|---|
| `audio` | file | Yes | The recorded audio clip |
| `language` | string | No | ISO-639-1 code (`en`, `hi`, `pa`, `ta`, `te`, `bn`). Omit to auto-detect. |

**Response** — `200 OK`

```json
{
  "transcript": "Patient in bed four, vitals stable overnight...",
  "detected_language": "en",
  "language_probability": 0.994
}
```

Silence returns `"(no speech detected)"` rather than an empty string. Failures return `500` with a `detail` field describing the cause, which the frontend displays directly to the user.

### `GET /`

Health check. Returns `{"status": "ok", "message": "..."}`.

---

## Documentation

| Deliverable | Location |
|---|---|
| Project proposal (PDF + LaTeX source) | [`proposal/`](proposal/) |
| Data flow diagrams — Level 0, 1, 2 | [`doc/UML Diagrams/NurseSync_DFD.pdf`](doc/UML%20Diagrams/NurseSync_DFD.pdf) |
| Entity-relationship diagram | [`doc/UML Diagrams/ER_Diagram.drawio.pdf`](doc/UML%20Diagrams/ER_Diagram.drawio.pdf) |
| UML use case diagram | [`doc/UML Diagrams/UML_NurseSync_UserCase.drawio-4.pdf`](doc/UML%20Diagrams/UML_NurseSync_UserCase.drawio-4.pdf) |
| Activity diagram | [`doc/UML Diagrams/NurseSync_Activity_Diagram.pdf`](doc/UML%20Diagrams/NurseSync_Activity_Diagram.pdf) |
| Presentation deck | [`doc/NurseSync.pptx`](doc/NurseSync.pptx) |
| Weekly progress journals | [`journals/`](journals/) |

---

## Team

| Member | Roll No | Responsibilities |
|---|---|---|
| Shivansh Sharma | 1024030732 | Proposal finalisation, ER diagram, `/transcribe` endpoint, repository structure, GitHub Pages deployment, local HTTPS |
| Ishaan Bhalla | 1024030950 | Proposal content, Level 0 & Level 1 DFDs, README, FastAPI setup and faster-whisper integration, end-to-end testing |
| Pushp Batheja | 1024030941 | UML and activity diagrams, speech-to-text frontend — microphone capture, live states, transcript display |

---

## Roadmap

Persist handoffs to PostgreSQL using the seven-entity schema already modelled in the ER diagram, replacing browser storage. Add medical entity extraction over the transcript, then structure each handoff automatically into **SBAR** format (Situation, Background, Assessment, Recommendation) with a completeness score that flags missing fields. Populate the patient timeline from saved handoffs and implement the deterioration risk classifier that surfaces at-risk patients to the incoming nurse. Replace the demo login with real authentication and role-based access, and benchmark word error rate against an annotated clinical speech set.
