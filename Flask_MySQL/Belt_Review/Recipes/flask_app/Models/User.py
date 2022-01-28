from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask import flash

class Users:
    def __init__(self, data):
        self.id = data['ID']
        self.First_Name = data['First_Name']
        self.Last_Name = data['Last_Name']
        self.Email = data ['Email']
        self.Password = data['Password']
        self.Created_At = data['Created_At']
        self.Updated_At = data['Updated_At']

# Get One User
    @classmethod
    def GetOne(cls, data):
        query = 'SELECT * FROM Users WHERE ID = %(ID)s'
        results = connectToMySQL('Users').query_db(query,data)
        return cls(results[0])

# Create New User
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO Users (First_Name, Last_Name, Email, Password, Created_At, Updated_At) VALUES (%(First_Name)s, %(Last_Name)s, %(Email)s, %(Password)s, NOW(), NOW())"
        return connectToMySQL('Recipe').query_db(query, data)

# FLASH
    @staticmethod
    def ValidateUser(user):
        is_valid = True
        if len(user['First_Name']) < 3:
            flash("First Name must be longer than 3 characters")
            is_valid = False
        if len(user['Last_Name']) < 3:
            flash("Last Name must be longer than 3 characters")
            is_valid = False
        if len(user['Email']) < 3:
            flash("Email must by longer than 3 characters")
            is_valid = False
        if len(user['Password']) < 3:
            flash("Password must be longer than 3 characters")
            is_valid = False