#!/usr/bin/python3
# Python script that fetches id from api.github.com/users
if __name__ == "__main__":
    import requests as res
    from sys import argv
    try:
        r = res.get('https://api.github.com/user', auth=(argv[1], argv[2]))
        print(r.json().get('id'))
    except BaseException:
        pass
