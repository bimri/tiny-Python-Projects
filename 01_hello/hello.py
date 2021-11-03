#!/usr/bin/env python
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Salimiana')
parser.add_argument('-j', '--jina', metavar='jina',
                    default='Dunia', help='Jina la kusalimia')
args = parser.parse_args()
print('Habari, ' + args.jina + '!')


'''
The argument is now optional and no longer a
positional argument. It’s common to provide both
short and long names to make it easy to type the
options. The metavar value of “name” appears here
to describe what the value should be.
'''


"""
Remember that parameters that
start with dashes are optional, so they can be left out, and they may have default values.
Parameters that don’t start with dashes are positional and are usually required, so they
do not have default values.
"""
