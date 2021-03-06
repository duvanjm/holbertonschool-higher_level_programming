#!/usr/bin/python3

"""show cities
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    row = cur.fetchall()
    data = []
    for cit in row:
        data.append(cit[0])
    print(', '.join(data))
    cur.close()
    conn.close()
