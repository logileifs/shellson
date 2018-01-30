#!/usr/bin/env python
import argparse
from contextlib import contextmanager
import unittest
import mock
import json
import sys

# StringIO module is not available in python3
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from shellson.__main__ import main


# Context manager function to capture stdout
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def mock_read_stdin():
    return json.dumps({'param1': 'value1'})


class TestMain(unittest.TestCase):
    """unit tests for shellson __main__.py"""
    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='get', key='param1', file=None, pretty=False))
    @mock.patch('shellson.__main__.read_stdin', new=mock_read_stdin)
    def test_get(self, args):
        with captured_output() as (out, err):
            main()
            output = out.getvalue().strip()
        assert json.loads(output) == 'value1'


    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='get', key='param1', file='test/simple.json', pretty=False))
    def test_file(self, args):
        with captured_output() as (out, err):
            main()
            output = out.getvalue().strip()
        assert json.loads(output) == 'value1'
