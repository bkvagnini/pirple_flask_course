from flask import Flask, render_template, request, session, redirect, url_for, g
# session, redirect, url_for, g are new
import model

app = Flask(__name__)
app.secret_key = 'jumpingjacks' # this is just for demo purposes - needs to be a string

username = ''
user = model.check_users()


#@app.route('/', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET'])
def home():
    if 'username' in session:
        g.user = session['username'] #g is the global variable for Flask
        return render_template('index2.html') 
    return render_template('home.html', message = "Log in or sign up")

 @app.route ('/login', methods = ['GET', 'POST'])
 def login():
     if request.method == 'POST':
         session.pop('username', None)
         areyouuser = request.form ['username']
         pwd = model.check_pw(areyouuser)
         if request.form['password'] == pwd:
             session['username'] = request.form['username']
             return redirect(url_for('home')) # this string home refers to the home function up above

'''   
def home(): # original home function
    if request.method == "GET":
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        #this will normally go into a db
        db_password = model.check_pw(username)
        if password == db_password:
        #if username == "Gordon" and password == "Ramsey":
            #message = model.show_task('Gordon')
            message = model.show_color(username) 
            #this is pulling task from db based on user
            #return render_template('index2.html', message = 'Login Successful')
            return render_template('index2.html', message = message)
        else:
            error_message = 'You have provided the wrong username and password combination...'
            return render_template('index.html', message = error_message)
'''

@app.route('/signup', methods = ['GET', 'POST']) # Have to add the POST method once you creeate the signup.html page 
def signup():
    if request.method == 'GET':
        message = 'Please sign up for our service.'
        return render_template('signup.html', message = message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        favorite_color = request.form["favorite_color"]
        message = model.signup(username, password, favorite_color)
        return render_template('signup.html', message = message)

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('contact.html')

if __name__ =='__main__':
    app.run(port = 7000, debug = True)


