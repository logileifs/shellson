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

upload:
	twine upload dist/$(shell ls dist/ | tail -1)

release: test clean build upload