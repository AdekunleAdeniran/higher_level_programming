#!/usr/bin/python3
# Python script that fetches a url using only requests
if __name__ == "__main__":
    import requests as req
    r = req.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(r.text), r.text))
