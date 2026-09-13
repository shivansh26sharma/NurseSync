.PHONY: setup run

VENV := .venv
DEMO_DIR := code/speech-to-text-demo

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r $(DEMO_DIR)/requirements.txt

run:
	cd $(DEMO_DIR) && ../../$(VENV)/bin/uvicorn server:app --reload
