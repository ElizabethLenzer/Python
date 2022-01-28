from crypt import methods
from flask import render_template, request, redirect, session, flash
from flask_app.Models.User import Users
from flask_bcrypt import Bcrypt # the class
from flask_app import app

bcrypt = Bcrypt(app) #Instantiate an object/instance of the Bcrypt class

@app.route('/')
def home():
    if "UUID" in session:
        return redirect('/Users')
    return render_template('Home.html', user = Users.GetOne({'ID': session['UUID']}))

@app.route('/users')
def ShowUsers():
    return render_template('AddRecipe.html')

@app.route('/InsertUser', methods = ['POST'])
def register():
    if not Users.ValidateUser(request.form):
        return redirect('/')
    #Hash Password
    Phash = Bcrypt.generate_password_hash(request.form['Password'])
    user_data= {
        **request.form,
        'Password': Phash
    }
    user_id = Users.create(user_data)
    session["UUID"] = user_id
    return redirect('/AddRecipe')

@app.route('/login', methods = ['POST'])
def login():
    if not Users.LoginValidation(request.form):
        return redirect('/')
    user = Users.GetByEmail({'Email': request.form['Email']})
    session['UUID'] = user.id

    return redirect('/AddRecipe')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')