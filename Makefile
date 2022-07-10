setup:
	python3 -m venv ~/.udacity-devops

install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	python -m pytest -vv test_hello.py

lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203,W0702 app.py
	pylint --disable=R,C hello.py

all: install lint test
