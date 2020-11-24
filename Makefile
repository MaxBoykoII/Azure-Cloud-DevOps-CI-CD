
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest "project/tests"

lint:
	pylint --disable=R,C hello.py

all: install lint test