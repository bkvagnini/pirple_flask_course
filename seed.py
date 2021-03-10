import sqlite3
# review https://docs.python.org/3/library/sqlite3.html

#connection = sqlite3.connect('Flask_tut.db', check_same_tread = False)
connection = sqlite3.connect('Flask_tut.db', check_same_thread = False)

cursor = connection.cursor()
cursor.execute(
""" INSERT INTO users (
    username, password, favorite_color
    ) VALUES (
    'Gordon', 'Ramseay', 'Red'
  );"""
)

cursor.execute(
""" INSERT INTO users (
    username, password, favorite_color
    ) VALUES (
    'Ironman', 'Tony', 'Gold'
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