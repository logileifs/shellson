.PHONY: build dist test

build:
	python setup.py sdist

dist: build

clean:
	rm -rf dist/
	rm -rf shellson.egg-info/

test:
	nosetests test/

install:
	echo "no requirements to install"