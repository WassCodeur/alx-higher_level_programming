#!/usr/bin/python3
"""myql module"""
import MySQLdb
import sys


if __name__ == "__main__":
    search = '{}'.format(sys.argv[4])
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                WHERE states.name = %s\
                ORDER BY states.id ASC",
                (search,))
    states = cur.fetchall()
    for stat in states:
        print(stat)
    cur.close()
    conn.close()
