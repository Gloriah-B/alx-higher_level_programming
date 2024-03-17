#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(username, password, database_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database_name, port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to fetch states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
