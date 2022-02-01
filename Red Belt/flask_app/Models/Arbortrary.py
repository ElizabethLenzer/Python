from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask import flash
from flask_app.Models.User import Users
from flask_app.Models import User

class Arbortraries:
    schema ='Arbortrary'
    def __init__(self, data):
        self.ID = data['ID']
        self.Species = data['Species']
        self.Location = data['Location']
        self.Reason = data['Reason']
        self.Date_Planted = data['Date_Planted']
        self.Created_At = data['Created_At']
        self.Updated_At = data['Updated_At']
        self.User_ID = data['User_ID']
        self.creator = Users.GetOne({"ID": data["User_ID"]})

# Get One Arbortrary
    @classmethod
    def GetOne(cls, data):
        query = 'SELECT * FROM Arbortrary WHERE ID = %(ID)s'
        results = connectToMySQL(cls.schema).query_db(query,data)
        return cls(results[0])

# Get All Arbortraries
    @classmethod
    def GetAll(cls):
        query = "SELECT * FROM Arbortrary"
        results = connectToMySQL(cls.schema).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users


# Create New Arbortrary
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO Arbortrary (Species, Location, Reason, Date_Planted, Created_At, Updated_At, User_ID) VALUES (%(Species)s, %(Location)s, %(Reason)s, %(Date_Planted)s, NOW(), NOW(), %(User_ID)s)"
        return connectToMySQL(cls.schema).query_db(query, data)

# Update Arbortrary
    @classmethod
    def Update(cls, data):
        query = "UPDATE Arbortrary SET Species = %(Species)s, Location = %(Location)s, Reason = %(Reason)s, Date_Planted = %(Date_Planted)s, Updated_At = NOW() WHERE ID = %(ID)s;"
        return connectToMySQL(cls.schema).query_db(query, data)

# Delete Arbortrary
    @classmethod
    def Delete(cls, data):
        query  = "DELETE FROM Arbortrary WHERE ID = %(ID)s"
        return connectToMySQL(cls.schema).query_db(query,data)

# Recipe Validation
    @staticmethod
    def ValidateArbortrary(post_data):
        is_valid = True
        print(post_data)

        if len(post_data["Species"]) < 3:
            flash("Species Must Be Longer Then Two Characters", "Arbortrary")
            is_valid = False

        if len(post_data["Location"]) < 3:
            flash("location Must Be Longer Then Two Characters", "Arbortrary")
            is_valid = False

        if len(post_data['Reason']) > 50:
            flash('Please Enter A Reason That Is Less Then 50 Char.', 'Arbortrary')
            is_valid = False

        return is_valid