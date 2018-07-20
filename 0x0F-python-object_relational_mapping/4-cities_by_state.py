#!/usr/bin/python3
"""
Python scripte to list items from MySQL
"""

import MySQLdb

from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER by cities.id")
    for rows in c.fetchall():
        print(rows)

    c.close()
    db.close()
