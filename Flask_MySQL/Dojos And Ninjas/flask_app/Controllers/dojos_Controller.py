from flask import render_template, request, redirect
from flask_app.Models.dojo import Dojos
from flask_app import app

# ---------------------------- Models = Crud ----------------------------------------------
# flask is a framework but a light frame work
# import things as we need them

@app.route('/')
def Home():
    dojos = Dojos.GetAll()
    return render_template('Dojo.html', dojos = dojos)

@app.route('/dojo/<int:Dojo_Id>')
def AddDojoMain(Dojo_Id):
    DojoDictionary={'ID':Dojo_Id}
    return render_template('Show_Ninja.html', dojos = Dojos.get_ninjas(DojoDictionary))

@app.route('/InsertDojo', methods=['POST'])
def ReRouteDojos():
    data = {"Name":request.form["Name"]}
    Dojos.CreateNew(data)
    return redirect('/')