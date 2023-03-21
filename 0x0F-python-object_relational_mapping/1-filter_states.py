#!/usr/bin/python3
"""myql module"""
import MySQLdb
import sys


conn = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=sys.argv[1],
                       passwd=sys.argv[2],
                       db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
states = cur.fetchall()
for state in states:
    print(state)
