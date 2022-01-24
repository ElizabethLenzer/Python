from mySQLConnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['ID']
        self.first_name = data['First_Name']
        self.last_name = data['Last_Name']
        self.email = data['Email']
        self.created_at = data['Created_At']
        self.updated_at = data['Updated_At']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( First_Name , Last_Name , Email , Created_At, Updated_At ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE ID = %(id)s;"
        user_dict = connectToMySQL('users_schema').query_db(query, data)
        return cls(user_dict[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET First_Name=%(first_name)s, Last_Name = %(last_name)s, Email = %(email)s, Updated_at = NOW() WHERE ID = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE ID = %(id)s"

        connectToMySQL('users_schema').query_db(query, data)