#!/usr/bin/env python
import argparse
import json
import sys


def json_to_dict(json_data):
    return json.loads(json_data)


def read_stdin():
    json_data = sys.stdin.read()
    return json_data


def read_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def main():
    parser = argparse.ArgumentParser(description='Parse json on command line', prog='shellson')
    parser.add_argument('command', help='get: to get value or type: to get type of value')
    parser.add_argument('key')
    parser.add_argument('-f', '--file', help='path of the json file to read')
    parser.add_argument('-p', '--pretty', dest='pretty', action='store_true', help='activate pretty print')
    args = parser.parse_args()
    if args.file == None:
        json_data = read_stdin()
        data = json.loads(json_data)
    else:
        data = read_file(args.file)

    value = data.get(args.key, None)
    if args.command == 'get' and args.pretty:
        print(json.dumps(value, indent=4))
    elif args.command == 'get':
        print(json.dumps(value))

    if args.command == 'type':
        print(str(type(value)))


if __name__ == '__main__':
    main()
