#!/usr/bin/python3
"""myql module"""
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
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                WHERE states.name = \'{}\'\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC".format(state))
    cities = cur.fetchall()
    for citie in cities:
        print(citie)
    cur.close()
    conn.close()
