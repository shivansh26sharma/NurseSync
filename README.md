# NurseSync AI

Intelligent audio-based clinical handoff system. See `docs/proposal.docx` (or your submitted proposal) for the full project description.

## 6-week build plan

| Week | Deliverable |
|---|---|
| 1 | Repo scaffold, FastAPI backend, PostgreSQL models (Patient, Handoff, Vitals, Medication, TimelineEvent, RiskPrediction), CI (lint + tests) |
| 2 | JWT auth (login), patient CRUD endpoints, tests |
| 3 | Handoff data model + manual entry endpoints, completeness checks |
| 4 | Flutter app shell (login, patient list, patient profile) wired to the backend |
| 5 | Audio recording/upload + storage |
| 6 | Whisper speech-to-text integration + transcript display |

This week's code lives in `backend/`. No AI/ML, auth, or Flutter code yet — those are Weeks 2+.

## Project structure

```
nursesync-ai/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routers (just /health this week)
│   │   ├── core/         # settings/config
│   │   ├── db/           # SQLAlchemy session + declarative base
│   │   ├── models/       # ORM models: Patient, User, Handoff, Vitals, Medication, TimelineEvent, RiskPrediction
│   │   └── main.py       # FastAPI app entrypoint
│   ├── alembic/          # DB migrations
│   ├── tests/            # pytest suite (runs against in-memory SQLite)
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml    # optional: backend + Postgres in one command, once Docker is installed
└── .github/workflows/ci.yml
```

## Running it locally (no Docker required)

You confirmed Docker isn't installed yet, so here's the plain path. (If you install Docker Desktop later, `docker compose up` from the repo root does everything in one step instead.)

**1. Install PostgreSQL** (one-time, via Homebrew):
```bash
brew install postgresql@16
brew services start postgresql@16
createuser -s nursesync
createdb -O nursesync nursesync
psql -d nursesync -c "ALTER USER nursesync WITH PASSWORD 'nursesync';"
```
(No Homebrew? Install it first from https://brew.sh, or use Postgres.app from https://postgresapp.com instead.)

**2. Set up the backend:**
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
```

**3. Run the database migration** (creates all tables):
```bash
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

**4. Start the API:**
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/health and http://localhost:8000/docs (interactive API docs).

**5. Run tests and lint** (what CI runs on every push):
```bash
pytest -v
ruff check .
```

## Pushing this week's update to GitHub

From the `nursesync-ai/` folder:

```bash
git init                     # skip if this folder is already a git repo
git add .
git commit -m "Week 1: repo scaffold, FastAPI backend, PostgreSQL models, CI"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

If the remote already has commits (repo wasn't empty), use `git pull --rebase origin main` before pushing, or `git push -u origin main --force` **only** if you're sure there's nothing important on the remote yet.

Check the **Actions** tab on GitHub after pushing — the CI workflow should run automatically and show green checks for lint + tests.

## Safety note

Uses synthetic/de-identified data only. The system is decision-support (summarization, retrieval, experimental risk scoring) — it does not diagnose or make autonomous clinical decisions.
