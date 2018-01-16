.PHONY: build

build:
	python setup.py sdist

clean:
	rm -rf dist/
	rm -rf shellson.egg-info/
