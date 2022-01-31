from flask import render_template, request, redirect, session, flash
from flask_app.Models.User import Users
from flask_bcrypt import Bcrypt # the class
from flask_app import app

bcrypt = Bcrypt(app) #Instantiate an object/instance of the Bcrypt class

@app.route('/')
def home():
    if "UUID" in session:
        return redirect('/Dashboard')
    return render_template('Home.html')

@app.route('/InsertUser', methods = ['POST'])
def register():
    if not Users.ValidateUser(request.form):
        return redirect('/')
    #Hash Password
    print(request.form['Password'])
    input_pw = {'password': request.form['Password']}
    Phash = bcrypt.generate_password_hash(input_pw['password'])
    user_data= {
        **request.form,
        'Password': Phash
    }
    user_id = Users.CreateNew(user_data)
    session["UUID"] = user_id
    return redirect('/Dashboard')

@app.route("/verify/login", methods=["POST"])
def verify_login():
    user_check = Users.GetByEmail({"Email": request.form["Email"]})
    if not Users.LoginValidation(user_check, {"InputPW": request.form["Password"]}):
        return redirect("/")
    session["UUID"] = user_check.ID
    flash("Logged In Successfully", "logged-in")
    return redirect("/Dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')