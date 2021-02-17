from flask import Flask

app = Flask(__name__)
@app.route('/', methods = ['GET'])

def home():
    return (
'<html><head><title>Demo</title></head><body><h1>The Thunderdome!</h1> <p> 2 men enter</p><p> 1 man leaves...</p></body></html>')

if __name__ =='__main__':
    app.run(port = 7000, debug = True)


