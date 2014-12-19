all: build

build: init
	@python setup.py bdist_wheel

init:
	@easy_install --upgrade setuptools
	@pip install -r requirements.txt

test: init
	@python setup.py test

clean:
	./clean.sh
