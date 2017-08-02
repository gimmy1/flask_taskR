import sqlite3
from _config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # now create table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)
    """)

    # insert dummy data into table
    c.execute(
        'INSERT INTO tasks(name, due_date, priority, status)'
        'VALUES("Finish this tutorial", "03/11/11", 1, 1)'
    )

    c.execute(
        'INSERT INTO tasks(name, due_date, priority, status)'
        'VALUES("Do not Finish this tutorial", "03/11/41", 10, 1)'
    )
