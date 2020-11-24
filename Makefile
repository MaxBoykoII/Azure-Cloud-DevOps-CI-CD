
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "project/tests"

lint:
	flake8 project

all: install lint test