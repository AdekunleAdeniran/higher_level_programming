#!/usr/bin/python3
# Python script that fetches a url and returns status code
if __name__ == "__main__":
    import requests as req
    from sys import argv

    r = req.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
