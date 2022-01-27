from flask import render_template, request, redirect
from flask_app.Models.User import Users
from flask_app import app

@app.rout('/')
def Home():
    return render_template('Home.html' user = User.GetAll())