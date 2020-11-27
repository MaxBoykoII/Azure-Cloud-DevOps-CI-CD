
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "src/tests"

lint:
	flake8 src

format:
	black src --check

all: install lint format test