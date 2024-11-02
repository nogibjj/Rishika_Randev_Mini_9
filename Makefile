install:
#installs requirements
	pip install --upgrade pip && pip install -r requirements.txt

format:
#formats files according to pep8
	black *.py

lint:
#checks to make sure Python files are formatted to industry standard
	ruff check *.py 

test:
#tests files
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

all:
#all of the above
	install format lint test
