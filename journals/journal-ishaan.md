# Weekly Progress Journal — Ishaan Bhalla (Roll No: 1024030950)

**Project Name:** NurseSync AI (Voice-Driven Nurse Shift Handoff System) **Role:** Requirements Documentation, System Modelling, & Speech-to-Text Backend

---

## Week 1 (Aug 3 - Aug 9): Project Inception & Ideation

- Formed the team with Shivansh Sharma and Pushp Batheja for the UCS503P Software Engineering project.
- Participated in the team's brainstorming sessions to finalise our project concept: **NurseSync AI**, a voice-driven nurse shift handoff system built around the tagline "Speak. Sync. Care."
- Researched the problem space — verbal nurse handovers are unstructured and rushed, making them a known source of clinical information loss — and confirmed it was a real problem worth solving.
- Reviewed candidate speech-to-text approaches to check that automatic transcription was feasible within our semester timeline and without a paid API.

## Week 2 (Aug 10 - Aug 16): Project README & Repository Documentation

- Wrote the project `README.md`, covering the problem statement, the proposed solution, the technology stack, and setup instructions for running the project locally.
- Structured the README so that a reader unfamiliar with the project could understand what NurseSync AI does and get it running without asking the team.
- Took ownership of keeping the README current, updating it as the stack and setup steps evolved through the semester.
- Set up my local git environment and agreed commit conventions with the team.

## Week 3 (Aug 17 - Aug 23): Project Proposal — Initial Draft

- Drafted the initial project proposal content, writing the substantive material the team's submission was built on.
- Articulated the problem statement and motivation, setting out why nurse handoffs are a clinically significant failure point and how an automated system addresses that.
- Wrote the objectives, proposed methodology, and expected outcomes sections, and documented the technology stack we had selected.
- Handed the completed draft to the team for formatting and final assembly into the submission document.

## Week 4 (Aug 24 - Aug 30): System Modelling — Data Flow Diagrams

- Designed the **Level 0 (Context) Data Flow Diagram**, establishing the system boundary and identifying the external entities that interact with NurseSync AI.
- Decomposed this into the **Level 1 (Detailed) Data Flow Diagram**, breaking the system into its core processes — audio capture, transcription, record structuring, and persistence — together with the data stores connecting them.
- Verified that every data flow in the Level 1 diagram balanced correctly against the context diagram, so the two levels stayed consistent with each other.
- Documented the design rationale behind the process decomposition so the diagrams could be carried directly into the project reports.

## Week 5 (Aug 31 - Sep 6): FastAPI Application & Whisper Model Integration

- Set up the FastAPI application that hosts the project's speech-to-text service, establishing the app structure, configuration, and CORS setup needed for the frontend to call it during development.
- Integrated the **faster-whisper** model for transcription, running it locally on CPU with int8 quantisation to keep it performant without a GPU.
- Chose a local model deliberately over a hosted transcription API: it requires no API key, incurs no per-request cost, and works fully offline once the model is cached — which matters for a hospital ward with unreliable connectivity.
- Confirmed the model's multilingual capability, covering English, Hindi, Punjabi, Tamil, Telugu, and Bengali with no additional setup, so the system suits a real Indian clinical setting.

## Week 6 (Sep 7 - Sep 13): End-to-End Testing & Verification

- Tested and verified the complete speech-to-text flow end to end: browser recording, upload to the backend, transcription, and display of the returned transcript in the UI.
- Validated the pipeline across multiple languages and recording lengths to confirm the model handled real spoken handoff content rather than only short test clips.
- Investigated and resolved issues surfaced during testing, including server startup and environment problems that prevented the demo from running reliably.
- Updated the README to reflect the final setup steps, and confirmed the system was reproducible from a clean checkout ahead of the prototype-stage evaluation.
