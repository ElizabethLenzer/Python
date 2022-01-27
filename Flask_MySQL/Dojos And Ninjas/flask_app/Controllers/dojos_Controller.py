from flask import render_template
from flask_app.Models.dojo import Dojos
from flask_app import app

# ---------------------------- Models = Crud ----------------------------------------------

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/Dojo')
def AddDojoMain():
    return render_template('Add_New_Dojo.html', dojo=Dojos.GetAll())

@app.route('/Insert', methods=['POST'])
def ReRoute():
    Dojos.save(request.form)
    return redirect('/')