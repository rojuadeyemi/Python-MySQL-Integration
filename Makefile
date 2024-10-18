SHELL := /bin/bash

.PHONY: all activate run

all: requirements.txt
	test -d .venv || python -m venv .venv
	source .venv/Scripts/activate && pip install -r requirements.txt
	touch .venv

activate:
	.venv\Scripts\activate

run:
	python main.py
