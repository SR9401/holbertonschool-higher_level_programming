#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the `states` table of `hbtn_0e_0_usa` where name matches the argument.

It uses MySQLdb to connect to a MySQL server and perform a SELECT query.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""
import MySQLdb
import sys


def list_states_with_name():
    """
    Connects to the MySQL database and fetches all rows from the
    `states` table where the name matches the argument passed.
    Results are sorted in ascending order by states.id.
    """
    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states_with_name()
