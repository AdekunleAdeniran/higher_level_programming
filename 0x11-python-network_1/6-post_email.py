#!/usr/bin/python3
# Python script that fetches a url and post email using only requests
if __name__ == "__main__":
    import requests as req
    from sys import argv

    r = req.post(argv[1], data={'email': argv[2]})
    print(r.text)
