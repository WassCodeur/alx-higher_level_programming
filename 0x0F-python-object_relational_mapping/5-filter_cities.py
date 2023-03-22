#!/usr/bin/python3
"""mysql module"""
import MySQLdb
import sys


if __name__ == "__main__":
    state = sys.argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT cities.name\
                 FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s", (state,))
    cities = cur.fetchall()
    num_cities = len(cities)
    for i, (city,) in enumerate(cities):
        if i == num_cities - 1:
            print(city)
        else:
            print(city, end=", ")
    cur.close()
    conn.close()
