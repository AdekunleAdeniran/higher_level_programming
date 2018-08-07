#!/usr/bin/python3
# Python script that fetches a url and post email using only requests
if __name__ == "__main__":
    import requests as res
    from sys import argv
    r = res.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    r = r.json()
    print("Number of results: {}".format(r['count']))
    for name in r['results']:
        print(name['name'])
