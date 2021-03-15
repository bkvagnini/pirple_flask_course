import sqlite3

def show_task(username):
    #connect the db
    connection = sqlite3.connect('ToDo.db', check_same_thread = False)
    cursor = connection.cursor()
    
    # SQL Query
    cursor.execute(""" SELECT task FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    task = cursor.fetchone()[0]

    #close the DB connection
    connection.commit()
    cursor.close()
    connection.close()

    message = " {task} ".format(task = task)
    return message