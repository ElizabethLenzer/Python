from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask import flash
from flask_app.Models.User import Users

class Recipes:
    schema ='recipe'
    def __init__(self, data):
        self.ID = data['ID']
        self.Name = data['Name']
        self.Description = data['Description']
        self.Instructions = data['Instructions']
        self.Date_Made_On = data['Date_Made_On']
        self.Created_At = data['Created_At']
        self.Updated_At = data['Updated_At']
        self.User_ID = data['User_ID']
        self.creator = Users.GetOne({"ID": data["User_ID"]})

# Get One Recipe
    @classmethod
    def GetOne(cls, data):
        query = 'SELECT * FROM Recipes WHERE ID = %(ID)s'
        results = connectToMySQL(cls.schema).query_db(query,data)
        return cls(results[0])

# Get All Recipes
    @classmethod
    def GetAll(cls):
        query = "SELECT * FROM Recipes"
        return connectToMySQL(cls.schema).query_db(query)

# Create New Recipe
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO Recipes (Name, Description, Instructions, Date_Made_On, Under_30_Minutes, Created_At, Updated_At, User_ID) VALUES (%(Name)s, %(Description)s, %(Instructions)s, %(Date_Made_On)s, %(Under_30_Minutes)s, NOW(), NOW(), %(User_ID)s)"
        return connectToMySQL(cls.schema).query_db(query, data)

# Update Recipe
    @classmethod
    def Update(cls, data):
        query = "UPDATE recipes SET Name = %(Name)s, Instructions = %(Instructions)s, Description = %(Description)s, Date_Made_On = %(Date_Made_On)s, Under_30_Minutes = %(Under_30_Minutes)s, Updated_At = NOW() WHERE ID = %(ID)s;"
        return connectToMySQL(cls.schema).query_db(query, data)

# Delete Recipe
    @classmethod
    def Delete(cls, data):
        query  = "DELETE FROM recipes WHERE ID = %(ID)s"
        return connectToMySQL(cls.schema).query_db(query,data)
        
# Recipe Validation
    @staticmethod
    def ValidateRecipe(post_data):
        is_valid = True
        print(post_data)

        if len(post_data["Name"]) < 3:
            flash("Name Must Be Longer Then Two Characters", "recipe")
            is_valid = False

        if len(post_data["Instructions"]) < 3:
            flash("Instructions Must Be Longer Then Two Characters", "recipe")
            is_valid = False

        if len(post_data['Description']) < 5:
            flash('Please Enter Valid Description Longer Then 5 Char.', 'recipe')
            is_valid = False

        if 'Under_30_Minutes' not in post_data:
            flash("Confirm If Recipe is Under 30 Minutes", "recipe")
            is_valid = False

        return is_valid

