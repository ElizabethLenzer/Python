from flask import render_template
from flask_app.Models.ninja import Ninjas
from flask_app import app

# ---------------------------- Models = Crud ----------------------------------------------

@app.route('/Ninja')
def AddDojoMain():
    return render_template('Add_New_Dojo.html', ninja=Ninjas.GetAll())

@app.route('/Insert', methods=['POST'])
def ReRoute():
    data = {"First_Name":request.form["First_Name"], "Last_Name":request.form["Last_Name"], "Age":request.form["Age"], "Dojo_Id":request.form["Dojo_Id"]}
    Ninjas.save (data)
    return redirect('/')