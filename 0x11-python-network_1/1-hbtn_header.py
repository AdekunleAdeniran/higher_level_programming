#!/usr/bin/python3
# Python script that displays getheader value

if __name__ == '__main__':
    import urllib.request as ur
    from sys import argv

    with ur.urlopen(argv[1]) as header:
        print(header.getheader('X-Request-Id'))
