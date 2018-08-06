#!/usr/bin/python3
# Python script that displays getheader value

import urllib.request as ur
from sys import argv

with ur.urlopen(argv[1]) as header:
    print(header.getheader('X-Request-Id'))
