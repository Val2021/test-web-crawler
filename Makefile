.PHONY: all

VENV_NAME?=venv
BIN=$(VENV_NAME)/bin
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

all: test lint build

test:
	${PYTHON} -m pytest

lint:
	${BIN}/pre-commit run -a

build:
	cd ibm_test && docker-compose up -d  --build
