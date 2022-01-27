from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask_app.Models import ninja

class Dojos:
    def __init__(self, data):
        self.id = data['ID']
        self.Name = data['Name']
        self.CreatedAt = data['CreatedAt']
        self.UpdatedAt = data['UpdatedAt']
        self.ninjas=[]

# Display All Dojos
    @classmethod
    def GetAll(cls):
        query = "SELECT * FROM dojos;"
        return connectToMySQL('Dojos_And_Ninjas').query_db(query)
        # dojos = []
        # for dojo in results:
        #     dojos.append(cls(dojo))
        # return dojos

# Get One Dojo
    @classmethod
    def GetOne(cls, data):
        query = "SELECT * FROM dojos WHERE ID = %(ID)s"
        results = connectToMySQL('Dojos_And_Ninjas').query_db(query, data)
        return cls(results[0])

# Add Dojos
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO dojos ( Name, CreatedAt, UpdatedAt) VALUES (%(Name)s, NOW(), NOW());"
        return connectToMySQL('Dojos_And_Ninjas').query_db(query, data)

# Get Ninjas In Dojos
    @classmethod
    def get_ninjas(cls, Dojo_Id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.ID = ninjas.Dojo_Id WHERE dojos.ID = %(ID)s;"
        results = connectToMySQL("Dojos_And_Ninjas").query_db(query, Dojo_Id)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "ID": row['ninjas.ID'],
                "First_Name": row['First_Name'],
                "Last_Name": row['Last_Name'],
                "Age": row['Age'],
                "CreatedAt": row['ninjas.CreatedAt'],
                "UpdatedAt": row['ninjas.UpdatedAt'],
                "Dojo_Id": row["Dojo_Id"]
            }
            dojo.ninjas.append(ninja.Ninjas(ninja_data))
        return dojo