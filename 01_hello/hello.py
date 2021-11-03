#!/usr/bin/env python
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Salimiana')
parser.add_argument('jina', help='Jina la kusalimia')
args = parser.parse_args()
print('Habari, ' + args.jina + '!')
