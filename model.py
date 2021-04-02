import sqlite3

def show_color(username):
    #connect the db
    connection = sqlite3.connect('Flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    
    # SQL Query
    cursor.execute(""" SELECT favorite_color FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    color = cursor.fetchone()[0]

    #close the DB connection
    connection.commit()
    cursor.close()
    connection.close()

    message = " '{username}'s favorite color is '{color}' ".format(username = username, color = color)
    return message

def check_pw(username):
    #connect the db
    connection = sqlite3.connect('Flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    
    # SQL Query
    cursor.execute(""" SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    #close the DB connection
    connection.commit()
    cursor.close()
    connection.close()
    return password


def signup(username, password, favorite_color):
    #connect the db
    connection = sqlite3.connect('Flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    
    # SQL Query checks to see if the user exists
    cursor.execute(""" SELECT password FROM users WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone() 

    #inserts the user data into db
    if exist is None:
        cursor.execute(
            """ INSERT INTO users (
    username, password, favorite_color
    ) VALUES (
    '{username}', '{password}', '{favorite_color}'
  );""".format(username = username, password = password, favorite_color = favorite_color))

        #close the DB connection
        connection.commit()
        cursor.close()
        connection.close()

    else:
        return ('User already exists')
    return 'You have successfully signed up!'