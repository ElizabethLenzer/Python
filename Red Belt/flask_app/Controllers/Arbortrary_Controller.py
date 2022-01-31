from flask import render_template, request, redirect, session
from flask_app.Models.Arbortrary import Arbortraries
from flask_app.Models.User import Users
from flask_app import app

# Dashboard
@app.route('/Dashboard')
def ShowArbortraries():
    return render_template('Dashboard.html', user = Users.GetOne({'ID': session['UUID']}), Arbortraries = Arbortraries.GetAll())

# EditArbortrary
@app.route('/Arbortrary/<int:Arbortrary_ID>')
def EditArbortrary(Arbortrary_ID):
    return render_template('Edit.html', Arbortraries.GetOne({'ID':Arbortrary_ID}))

@app.route('/UpdateArbortrary/<int:Arbortrary_ID>', methods = ["POST"])
def UpdateArbortrary(Arbortrary_ID):
        if not Arbortraries.ValidateArbortrary(request.form):
            return redirect('/Arbortrary/add')
        arbortrary_data = {
            **request.form,
            'ID': Arbortrary_ID
        }
        Arbortraries.Update(Arbortrary_ID)
        return redirect('/Dashboard')

# Add Arbortrary
@app.route('/Arbortrary/add')
def AddArbortrary():
    return render_template('Add.html')

@app.route('/AddArbortrary', methods = ['POST'])
def InsertRecipe():
        if not Arbortraries.ValidateArbortrary(request.form):
            return redirect('/Arbortrary/add')
        arbortrary_data = {
            **request.form,
            'User_ID': session['UUID']
        }
        Arbortraries.CreateNew(arbortrary_data)
        return redirect('/Dashboard')

# Show Specific Arbortrary
@app.route('/Arbortrary/profile/<int:Arbortrary_ID>')
def ShowRecipe(Arbortrary_ID):
    return render_template('Arbortrary.html', arbortrary=Arbortraries.GetOne({'ID':Arbortrary_ID}))

@app.route('/Arbortrary/delete/<int:Arbortrary_ID>')
def DeleteRecipe(Arbortrary_ID):
    arbortrary=Arbortraries.Delete({'ID':Arbortrary_ID})
    return redirect('/Dashboard')