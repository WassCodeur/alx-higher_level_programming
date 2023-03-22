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
    to_list = list(cities)
    length = (len(to_list) -1)
    for i in range(length):
        print(to_list[i], end=", ")
    print(to_list[length])
    cur.close()
    conn.close()
