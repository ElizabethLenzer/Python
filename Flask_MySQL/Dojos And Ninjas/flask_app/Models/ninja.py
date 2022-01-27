from flask_app.Config.mySQLConnection import connectToMySQL

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
    query = "INSERT INTO dojos ( First_Name, Last_Name, Age, CreatedAt, UpdatedAt) VALUES (%(name)s, NOW(), NOW() );"
    return connectToMySQL('Dojos_And_Ninjas').query_db(query, data)