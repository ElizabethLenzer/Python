from flask import render_template, request, redirect
from flask_app.Models.Recipe import Recipes
from flask_app import app

@app.route('/')
def home():
    return render_template('Home.html')