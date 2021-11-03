"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './hello.py'


def test_exits():
    """exists"""
    assert os.path.isfile(prg)


def test_runnable():
    """Runs using python3"""
    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


def test_executable():
    """Says 'Hello, World!' by default"""
    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'


def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')
    

def test_input():
    """test for input"""
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'


'''
I’ve written the tests in an order that I hope will help you write the program in a logical
fashion. If the program doesn’t pass one of the tests, there’s no reason to continue
running the tests after it. I recommend you always run the tests with the flags -x, to
stop on the first failing test, and -v, to print verbose output. You can combine these
like -xv or -vx.
'''
  