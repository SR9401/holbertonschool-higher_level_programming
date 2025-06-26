#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.

"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    connects at database
    """
    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
