from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_Bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

class Users:
    schema = 'bands'
    def __init__(self, data):
        self.ID = data['ID']
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
        results = connectToMySQL(cls.schema).query_db(query,data)
        return cls(results[0])

# Get By Email
    @classmethod
    def GetByEmail(cls, data):
        query = "SELECT * FROM Users WHERE Email = %(Email)s"
        results = connectToMySQL(cls.schema).query_db(query,data)
        if results:
            return cls(results[0])

# Create New User
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO Users (First_Name, Last_Name, Email, Password, Created_At, Updated_At) VALUES (%(First_Name)s, %(Last_Name)s, %(Email)s, %(Password)s, NOW(), NOW())"
        return connectToMySQL(cls.schema).query_db(query, data)

# FLASH
    @staticmethod
    def ValidateUser(user):
        is_valid = True
        if len(user['First_Name']) < 2:
            flash("First Name must be longer than 2 characters")
            is_valid = False

        if len(user['Last_Name']) < 2:
            flash("Last Name must be longer than 2 characters")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user['Email']):
            flash("Invalid Email Address")
            is_valid = False
        elif Users.GetByEmail({"Email": user['Email']}):
            flash("Email is already in use")
            is_valid = False

        if len(user['Password']) < 8:
            flash("Password must be longer than 8 characters")
            is_valid = False
        elif user['Password'] != user['Confirm_Password']:
            flash("Passwords Dont Match", "register")
            is_valid = False
        return is_valid

# FLASH LOGIN VALIDATION
    @staticmethod
    def LoginValidation(user, InputPW):
        is_valid = True
        
        print(user, InputPW)
        if not user:
            flash("Invalid Email or Passowrd", "Login")
            is_valid = False
            return is_valid
        
        if not bcrypt.check_password_hash(user.Password, InputPW['InputPW']):
            flash('Invalid Password', 'Login')
            is_valid = False

        return is_valid