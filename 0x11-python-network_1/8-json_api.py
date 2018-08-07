#!/usr/bin/python3
# Python script that fetches a url and post email using only requests
if __name__ == "__main__":
    import requests as req
    from sys import argv
    try:
        letter = argv[1]
    except BaseException:
        letter = ""
    try:
        r = req.post('http://0.0.0.0:5000/search_user', data={'q': letter})
        r = r.json()
        r_id = r.get('id')
        r_name = r.get('name')
        if r_id is None or r_name is None:
            print('No result')
        else:
            print('[{}] {}'.format(r_id, r_name))
    except BaseException:
        print('Not a valid JSON')
