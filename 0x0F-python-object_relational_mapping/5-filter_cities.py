#!/usr/bin/python3

"""lists all cities from the database hbtn_0e_4_usa
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
    dataRow = cur.fetchall()
    listData = []
    for name in dataRow:
        listData.append(name[0])
    print(', '.join(listData))
    cur.close()
    conn.close()
