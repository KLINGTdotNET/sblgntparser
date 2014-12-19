all: build

build: init
	@python setup.py bdist_wheel

init:
	@pip install -r requirements.txt

test: init
	@python setup.py test

clean:
	./clean.sh
