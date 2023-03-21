#!/usr/bin/python3
"""myql module"""
import MySQLdb
import sys


# get arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]
conn = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=username,
                       passwd=password,
                       db=database)
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
            (state_name,))
states = cur.fetchall()
for state in states:
    print(state)
