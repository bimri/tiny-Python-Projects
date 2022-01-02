#!/usr/bin/env python 
"""tests for jump.py"""

import os 
from subprocess import getstatusoutput

prg = './jump.py'


def test_exists():
    """exists"""
    assert os.path.isfile(prg)

