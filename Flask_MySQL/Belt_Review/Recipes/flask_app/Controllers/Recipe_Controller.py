from flask import render_template, request, redirect, session
from flask_app.Models.Recipe import Recipes
from flask_app.Models.User import Users
from flask_app import app

@app.route('/Dashboard')
def ShowRecipes():
    return render_template('Dashboard.html', user = Users.GetOne({'ID': session['UUID']}), Recipes = Recipes.GetAll())

@app.route('/recipe/<int:Recipe_ID>')
def EditRecipe(Recipe_ID):
    return render_template('EditRecipe.html', recipe=Recipes.GetOne({'ID':Recipe_ID}))

@app.route('/UpdateRecipe/<int:Recipe_ID>', methods = ["POST"])
def UpdateRecipe(Recipe_ID):
        if not Recipes.ValidateRecipe(request.form):
            return redirect('/recipe/add')
        recipe_data = {
            **request.form,
            'ID': Recipe_ID
        }
        Recipes.Update(recipe_data)
        return redirect('/Dashboard')

@app.route('/recipe/add')
def AddRecipe():
    return render_template('AddRecipe.html')

@app.route('/AddRecipe', methods = ['POST'])
def InsertRecipe():
        if not Recipes.ValidateRecipe(request.form):
            return redirect('/recipe/add')
        recipe_data = {
            **request.form,
            'User_ID': session['UUID']
        }
        Recipes.CreateNew(recipe_data)
        return redirect('/Dashboard')

@app.route('/recipe/profile/<int:Recipe_ID>')
def ShowRecipe(Recipe_ID):
    return render_template('Recipe.html', recipe=Recipes.GetOne({'ID':Recipe_ID}))

@app.route('/recipe/delete/<int:Recipe_ID>')
def DeleteRecipe(Recipe_ID):
    recipe=Recipes.Delete({'ID':Recipe_ID})
    return redirect('/Dashboard')
