all: init test build

build:
	@python setup.py bdist_wheel

init:
	@pip install -r requirements.txt

test:
	@python setup.py test

clean:
	./clean.sh
