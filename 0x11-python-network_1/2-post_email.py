#!/usr/bin/python3
# Python script to PORT to URL
if __name__ == "__main__":
    import urllib.request as ur
    import urllib.parse as urp
    from sys import argv

    value = {'email': argv[2]}
    data = urp.urlencode(value)
    data = data.encode('ascii')  # data should be bytes
    req = ur.Request(argv[1], data)
    with ur.urlopen(req) as response:
        print(str(response.read(), 'utf-8'))
