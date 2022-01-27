from flask_app.Configuration.mySQLConnection import connectToMySQL

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
        results = connectToMySQL('Recipe').query_db(query,data)
        return cls(results[0])

