from ast import Num
from flask import Flask 

app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route("/dojo")
def dojo():
    return "dojo"

@app.route("/say")
def say():
    return "Hi"

@app.route("/say/<name>")
def say(name):
    print(name)
    return "hi, " + name

@app.route("/repeat/<string:words>/<int:num>")
def repeat(words, num):
    return words * num

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.