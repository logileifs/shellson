#!/usr/bin/env python
import json
import sys


def json_to_dict(json_data):
    return json.loads(json_data)


def read_stdin():
    json_data = sys.stdin.read()
    return json_data


def main(command, key):
    json_data = read_stdin()
    data = json.loads(json_data)
    value = data.get(key, None)

    if command == 'get':
        print(json.dumps(value))

    if command == 'type':
        print(str(type(value)))


if __name__ == '__main__':
    try:
        command = sys.argv[1]
        key = sys.argv[2]
    except IndexError:
        raise SystemExit('no command specified')
    main(command, key)
