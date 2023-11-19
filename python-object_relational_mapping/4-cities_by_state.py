#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        db=argv[3]
    )

    db_cursor = db.cursor()
    db_cursor.execute("SELECT id, cities.name, states.name FROM cities "
                        + "INNER JOIN states ON states.id = cities.state_id")

    q_rows = db_cursor.fetchall()
    for i in q_rows:
        print(i)

    db_cursor.close()
    db.close()
