import sqlite3
# review https://docs.python.org/3/library/sqlite3.html

connection = sqlite3.connect('ToDo.db', check_same_thread = False)

cursor = connection.cursor()
cursor.execute(
""" INSERT INTO users (
    username, password, task
    ) VALUES (
    'Gordon', 'Ramseay', 'Learn Flask'
  );"""
)

cursor.execute(
""" INSERT INTO users (
    username, password, task
    ) VALUES (
    'Ironman', 'Tony', 'Get stuff done'
  );"""
)

connection.commit()
cursor.close()
connection.close()

# to check the database via CLI
#in Terminal, type in "sqlite3 Flask_tut.db"
#this presents a prompt "sqlite>"
# at this prompt, type in ".tables"
#this will display all tables in the database
# to run a query, type "select * from users;"
# Ctrl + D to exit sqlite>