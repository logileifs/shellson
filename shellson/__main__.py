#!/usr/bin/env python
import argparse
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
    parser = argparse.ArgumentParser(description='Parse json on command line', prog='shellson')
    parser.add_argument('command', help='get: to get value or type: to get type of value')
    parser.add_argument('key')
    parser.add_argument('-f', '--file', help='path of the json file to read')
    args = parser.parse_args()
    main(args.command, args.key)
