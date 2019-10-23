PKG=api

.PHONY: init flake8 pylint lint test clean

init: clean
	pipenv --python 3.7
	pipenv install --dev

flake8:
	pipenv run flake8

pylint:
	pipenv run pylint $(PKG) --ignore=tests

black:
	pipenv run black $(PKG) --skip-string-normalization

lint: flake8 pylint

test:
	pipenv run pytest $(PKG)/

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml

