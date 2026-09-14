# Weekly Progress Journal — Pushp Batheja (Roll No: 1024030941)

**Project Name:** NurseSync AI (Voice-Driven Nurse Shift Handoff System) **Role:** UML & Behavioural Modelling, & Speech-to-Text Frontend

---

## Week 1 (Aug 3 - Aug 9): Project Inception & Ideation

- Formed the team with Shivansh Sharma and Ishaan Bhalla for the UCS503P Software Engineering project.
- Participated in the team's brainstorming sessions to finalise our project concept: **NurseSync AI**, a voice-driven nurse shift handoff system built around the tagline "Speak. Sync. Care."
- Researched the problem space — verbal nurse handovers are unstructured and rushed, making them a known source of clinical information loss — and confirmed it was a real problem worth solving.
- Reviewed candidate speech-to-text approaches to check that automatic transcription was feasible within our semester timeline and without a paid API.

## Week 2 (Aug 10 - Aug 16): Repository Setup & Requirements Review

- Set up my local git environment and agreed commit conventions with the team.
- Reviewed the drafted requirements to understand the workflows I would be responsible for modelling, particularly the sequence a nurse follows when recording a handoff.
- Identified the system's actors and the actions available to each, as groundwork for the UML modelling in the following weeks.
- Studied the team's data flow diagrams so my behavioural models would stay consistent with the agreed process decomposition rather than diverging from it.

## Week 3 (Aug 17 - Aug 23): UML Modelling

- Designed the project's **UML diagrams**, committed to the repository's UML Diagrams documentation folder.
- Modelled the system's actors, their interactions, and the structural relationships between the core components of NurseSync AI.
- Kept the modelling consistent with the requirements captured in the project proposal, so the diagrams documented the system we had actually specified.
- Reviewed the diagrams with the team and revised them based on feedback before committing the final versions.

## Week 4 (Aug 24 - Aug 30): Activity Diagram

- Designed the **Activity Diagram** capturing the end-to-end nurse handoff workflow.
- Modelled the full control flow — starting a recording, capturing audio, submitting it for transcription, reviewing the returned transcript, and saving the completed handoff — including the decision points and alternative paths at each stage.
- Made the diagram reflect the real behaviour of the system rather than an idealised path, so it stayed useful as an implementation reference.
- Verified the modelled flow matched the processes in the team's Level 1 DFD, keeping the behavioural and data-flow views of the system aligned.

## Week 5 (Aug 31 - Sep 6): Speech-to-Text Frontend Page

- Built the speech-to-text frontend page — the project's one fully implemented HTML file — which serves as the working demo of the system.
- Laid out the patient context for the handoff (name, age, ward, attending doctor, and diagnosis) so a recording is always made against a clear clinical subject.
- Implemented **microphone capture** in the browser using the `MediaRecorder` API, requesting audio permission and collecting the recorded clip for upload to the backend.
- Added a language selector covering English, Hindi, Punjabi, Tamil, Telugu, and Bengali, with an auto-detect option, so the page could exercise the model's multilingual support.

## Week 6 (Sep 7 - Sep 13): Live Recording States & Transcript Display

- Implemented the page's **live state feedback** — a clear "Recording…" indicator while audio is being captured and a "Transcribing…" state while the backend processes the clip — so the user is never left uncertain whether the system is working.
- Built the **transcript display**, rendering the returned text in an editable field so a nurse can correct any transcription errors before the handoff is saved.
- Added handoff history on the page so previously saved handoffs for a patient remain visible, and surfaced backend failures as readable error messages instead of silent failures.
- Tested the interface end to end against the running backend — record, transcribe, review, save — and refined the states and styling ahead of the prototype-stage evaluation.
