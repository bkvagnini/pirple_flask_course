import sqlite3

connection = sqlite3.connect('ToDo.db', check_same_thread = False)

cursor = connection.cursor()
cursor.execute(
    """  CREATE TABLE users (
        user_pk Integer Primary Key AutoIncrement,
        username VARCHAR(16),
        password VARCHAR(32),
        task VARCHAR(32)
   ); 

      CREATE TABLE tasks (
        task_pk Integer Primary Key AutoIncrement,
        user_pk Integer,
        item VARCHAR(16),
        status VARCHAR(32)
    ); """
)

connection.commit()
cursor.close()
connection.close()
