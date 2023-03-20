#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv
    from MySQLdb import connect

    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    db = connect(host="localhost", user=username, password=password,
                 database=dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    res = cur.fetchall()
    for row in res:
        print(row)

    cur.close()