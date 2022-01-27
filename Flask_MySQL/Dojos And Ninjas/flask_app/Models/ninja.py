from flask_app.Configuration.mySQLConnection import connectToMySQL

class Ninjas:
    def __init__(self, data):
        self.id = data['ID']
        self.First_Name = data['First_Name']
        self.Last_Name = data['Last_Name']
        self.Age = data['Age']
        self.CreatedAt = data['CreatedAt']
        self.UpdatedAt = data['UpdatedAt']
        self.Dojo_Id = data['Dojo_Id']

    # Display All Ninjas
    @classmethod
    def GetAll(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('Dojos_And_Ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    # Add Ninjas
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO ninjas (First_Name, Last_Name, Age, CreatedAt, UpdatedAt, Dojo_Id) VALUES (%(First_Name)s, %(Last_Name)s, %(Age)s NOW(), NOW(),  %(Dojo_Id)s);"
        return connectToMySQL('Dojos_And_Ninjas').query_db(query, data)