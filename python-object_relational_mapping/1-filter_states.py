#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:

"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    connects at database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
