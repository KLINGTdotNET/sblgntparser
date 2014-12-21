all: build

build: init
	@python setup.py bdist_wheel

init:
	@easy_install --upgrade setuptools
	@pip install -r requirements.txt

test:
	@python setup.py test

clean:
	./clean.sh

pypi: init test build
	pandoc --from=markdown --to=rst README.md -o README.rst
	python setup.py bdist_wheel upload -r pypi
