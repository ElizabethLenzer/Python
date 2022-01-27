from flask_app.Configuration.mySQLConnection import connectToMySQL
from flask_app.Models import Book

class Authors:
    def __init__(self,data):
        self.id = data['ID']
        self.Name = data['Name']
        self.Created_At = data['Created_At']
        self.Updated_At = data['Updated_At']
        self.books = data[]

# Display All Authors
    @classmethod
    def GetAll(cls):
        query = "SELECT * FROM Authors"
        return connectToMySQL('Books').query_db(query)

# Get One Author
    @classmethod
    def GetOne(cls,data):
        query = "SELECT * FROM Authors WHERE ID = %(ID)s"
        results = connectToMySQL('Books').query_db(query,data)
        return cls(results[0])

# Add a New Author
    @classmethod
    def CreateNew(cls, data):
        query = "INSERT INTO dojos (Name, Created_At, Updated_At) VALUES (%(Name)s, NOW(), NOW();"
        return connectToMySQL('Books').query_db(query, data)

# Get Books in Authors
    @classmethod
    def get_books(cls, Author_ID):
        query = "SELECT * FROM Authors LEFT JOIN books on Authors.ID = books.Author_ID WHERE Authors.ID = %(ID)s"
        results = connectToMySQL('Books').query_db(query, Author_ID)
        Author = cls(results[0])
        for row in results:
            book_data = {
                'ID': row ['books.ID']
                'Name':
            }
