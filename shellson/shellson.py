#!/usr/bin/env python
import json
import sys


def read_stdin():
    incoming = sys.stdin.read()
    return json.loads(incoming)


def main():
    data = None
    command = sys.argv[1]
    parameter = sys.argv[2]
    data = read_stdin()
    if command == 'get-value':
        print(json.dumps(data.get(parameter)))

    if command == 'get-type':
        print(type(data.get(parameter)))


if __name__ == '__main__':
    main()
