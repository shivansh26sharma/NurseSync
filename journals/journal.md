# Weekly Progress Journal — Shivansh Sharma (Roll No: 1024030732)

**Project Name:** NurseSync AI (Voice-Driven Nurse Shift Handoff System) **Role:** Documentation & Diagrams, Speech-to-Text Backend, & Deployment

---

## Week 1 (Aug 3 - Aug 9): Project Inception & Ideation

- Formed the team with Ishaan Bhalla and Pushp Batheja for the UCS503P Software Engineering project.
- Participated in the team's brainstorming sessions to finalise our project concept: **NurseSync AI**, a voice-driven nurse shift handoff system built around the tagline "Speak. Sync. Care."
- Researched the problem space — verbal nurse handovers are unstructured and rushed, making them a known source of clinical information loss — and confirmed it was a real problem worth solving.
- Reviewed candidate speech-to-text approaches to check that automatic transcription was feasible within our semester timeline and without a paid API.

## Week 2 (Aug 10 - Aug 16): Repository Restructuring & Project Structure

- Restructured the team's GitHub repository to match the course-required project structure, aligning our folder layout with the prescribed template.
- Organised the repository into its required top-level directories so that documentation, source code, journals, and the staged project reports each had a clearly defined home.
- Set up my local git environment and agreed commit conventions with the team.

## Week 3 (Aug 17 - Aug 23): Project Proposal Documentation

- Formatted and finalised the project proposal into its final Word document, taking the team's drafted content through to a submission-ready deliverable.
- Applied consistent document structure throughout — heading hierarchy, typography, spacing, and table formatting — so the proposal read as a single professional document rather than merged drafts.
- Proofread the combined document and reconciled inconsistencies before the team submitted it.

## Week 4 (Aug 24 - Aug 30): Documentation Site & GitHub Pages Deployment

- Set up GitHub Pages deployment for the project, configuring a GitHub Actions workflow to build and publish the site automatically.
- Configured the workflow to trigger on pushes to the main branch and deploy the built output to the hosting branch, so the published page stays current without any manual step.
- Debugged the initial workflow runs and verified the deployed page rendered correctly at its public URL.

## Week 5 (Aug 31 - Sep 6): Speech-to-Text Backend — `/transcribe` Endpoint

- Built the `/transcribe` endpoint on the FastAPI backend, the core AI feature of the project.
- Implemented audio upload handling to receive the recorded clip as multipart form data and persist it server-side for processing.
- Wired the endpoint to the transcription model, including an optional language parameter so the caller can either specify the spoken language or let the model auto-detect it.
- Formatted the response into a clean JSON payload returning the transcript along with the detected language and its confidence score, and added error handling so failures surface as readable messages in the UI rather than silent errors.
- Loaded the model once and cached it in memory rather than per request, since reloading it on every call made transcription unacceptably slow.

## Week 6 (Sep 7 - Sep 13): ER Diagram, Local HTTPS & Hosted Demo Page

- Designed the complete **Entity-Relationship (ER) diagram** for the system, covering all entities with their key, multi-valued, and derived attributes, along with relationship attributes and cardinality constraints.
- Refined the diagram layout across several review iterations to remove connector overlaps and correct the cardinality on the Handoff–Patient relationship to many-to-one, and produced it in an editable draw.io format so the team can adjust it directly when assembling the final report.
- Set up local HTTPS using **mkcert** for the hosted demo page, generating a locally-trusted certificate for development.
- This was necessary because browsers only expose microphone access through `getUserMedia` on a secure context — without HTTPS the recording feature is blocked outright, so the demo could not run over plain HTTP.
- Verified the full pipeline end to end over the secure origin: record audio in the browser, upload to the backend, transcribe, and return the transcript, confirming successful responses from the endpoint.
- Consolidated the proposal, ER diagram, and deployed demo in preparation for the prototype-stage evaluation.
