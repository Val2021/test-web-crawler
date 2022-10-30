.PHONY: all

VENV_NAME?=venv
BIN=$(VENV_NAME)/bin
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

all: env dev build

env:
	python3 -m ${VENV_NAME} ${VENV_NAME}

dev:
	${BIN}/pip install -r requirements.txt

build:
	cd ibm_test && docker-compose up -d  --build
