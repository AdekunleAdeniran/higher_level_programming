#!/usr/bin/python3
# Python script that fetches a url and get header value using only requests
if __name__ == "__main__":
    import requests as req
    from sys import argv

    r = req.get(argv[1])
    print(r.headers.get('X-Request-Id'))
