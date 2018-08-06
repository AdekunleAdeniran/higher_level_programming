#!/usr/bin/python3
# Python script that fetches a url
import urllib.request as ur

with ur.urlopen('https://intranet.hbtn.io/status') as res:
    res = res.read()

print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(res), res))
print('\t- utf8 content: {}'.format(str(res, 'utf-8')))
