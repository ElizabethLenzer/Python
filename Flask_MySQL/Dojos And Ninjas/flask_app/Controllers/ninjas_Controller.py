import re
from flask import render_template, request, redirect
from flask_app.Models.ninja import Ninjas
from flask_app.Models.dojo import Dojos
from flask_app import app

# ---------------------------- Models = Crud ----------------------------------------------

@app.route('/NewNinja')
def NewNinja():
    return render_template('Add_Ninja.html', dojos = Dojos.GetAll())

@app.route('/InsertNinja', methods=['POST'])
def ReRouteNinjas():
    data = {"First_Name":request.form["First_Name"], 
    "Last_Name":request.form["Last_Name"], 
    "Age":request.form["Age"], 
    "Dojo_Id":request.form["Dojo_Id"]}
    Ninjas.CreateNew (data)
    return redirect('/')