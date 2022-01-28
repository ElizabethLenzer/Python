from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask import flash

class Recipes:
    def __init__(self, data):
        self.ID = data['ID']
        self.Name = data['Name']
        self.Description = data['Description']
        self.Instructions = data['Instructions']
        self.Date_Made = data['Date_Made']
        self.Created_At = data['Created_At']
        self.Updated_At = data['Updated_At']

# Get One Recipe
    @classmethod
    def GetOne(cls, data):
        query = 'SELECT * FROM Recipes WHERE ID = %(ID)s'
        results = connectToMySQL('Recipe').query_db(query,data)
        return cls(results[0])

# Create New Recipe
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO Users (Name, Description, Instructions, Date_Made, Created_At, Updated_At) VALUES (%(Name)s, %(Description)s, %(Instructions)s, %(Date_Made)s, NOW(), NOW())"
        return connectToMySQL('Recipe').query_db(query, data)