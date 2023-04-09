#!/usr/bin/python3
""" Lists all the states from hbtn_0e_0_usa db. """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN\
    states ON states.id=cities.state_id WHERE states.name=%s\
    ", (sys.argv[4],))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(*result, sep=", ")
    cursor.close()
    db.close()
