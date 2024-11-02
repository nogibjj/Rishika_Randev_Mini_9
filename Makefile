install:
#installs requirements
	pip install --upgrade pip && pip install -r requirements.txt

format:
#formats files according to pep8
	black *.py

lint:
#checks to make sure Python files are formatted to industry standard
	pylint --ignore-patterns=test_.*?py *.py

test:
#tests files
	python -m pytest -cov=main test_main.py

all:
#all of the above
	install format lint test
