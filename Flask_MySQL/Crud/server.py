from flask import Flask, render_template, request, redirect
from user import Users
app = Flask(__name__)    

@app.route('/')
def home():
    return render_template('index.html', users=Users.get_all())

@app.route('/AddUser')
def addUser():
    return render_template('AddUser.html')

@app.route('/insert', methods=['POST'])
def ReRoute():
    Users.save(request.form)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)