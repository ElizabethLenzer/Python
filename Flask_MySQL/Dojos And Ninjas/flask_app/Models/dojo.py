from flask_app.Configuration.mySQLConnection import connectToMySQL

class Dojos:
    def __init__(self, data):
        self.id = data['ID']
        self.Name = data['Name']
        self.CreatedAt = data['CreatedAt']
        self.UpdatedAt = data['UpdatedAt']

# Display All Dojos
@classmethod
def GetAll(cls):
    query = "SELECT * FROM dojos;"
    results = connectToMySQL('Dojos_And_Ninjas').query_db(query)
    dojos = []
    for dojo in results:
        dojos.append(cls(dojo))
    return dojos

# Add Dojos
@classmethod
def CreateNew(cls, data):
    query = "INSERT INTO dojos ( name, CreatedAt, UpdatedAt) VALUES (%(name)s, NOW(), NOW() );"
    return connectToMySQL('Dojos_And_Ninjas').query_db(query, data)