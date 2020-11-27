
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "src/tests"

lint:
	flake8 src &&\
		isort src --check-only

format:
	black src --check

all: install lint format test