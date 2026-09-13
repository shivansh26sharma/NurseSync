# NurseSync AI

Intelligent audio-based clinical handoff system.

## code/speech-to-text-demo

A standalone speech-to-text prototype: a nurse clicks Record, speaks a
patient handoff, and it's transcribed automatically using faster-whisper
(runs locally, no API key, no internet needed after the model is
downloaded once).

**Run it:**

```bash
make setup   # creates a venv and installs dependencies
```

Pre-download the Whisper model once (needs internet the first time):

```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0, 'code/speech-to-text-demo'); from server import get_model; get_model()"
```

Start the server:

```bash
make run
```

Then open `code/speech-to-text-demo/index.html` in a browser and click
**Record Handoff**.
