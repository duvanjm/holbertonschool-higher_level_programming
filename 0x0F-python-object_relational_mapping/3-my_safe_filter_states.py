#!/usr/bin/python3

"""show all values in the table of where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE Name =  %s ORDER BY id ASC",
                [sys.argv[4]])
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
