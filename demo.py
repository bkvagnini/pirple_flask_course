from flask import Flask, render_template, request
import model

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        #this will normally go into a db
        if username == "Gordon" and password == "Ramsay":
            message = model.show_color('Gordon') 
            #this is pulling color from db based on user
            #return render_template('index2.html', message = 'Login Successful')
            return render_template('index2.html', message = message)
        else:
            error_message = 'You have provided the wrong username and password combination...'
            return render_template('index.html', message = error_message)

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('contact.html')

if __name__ =='__main__':
    app.run(port = 7000, debug = True)


