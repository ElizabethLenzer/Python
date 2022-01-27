from flask_app import app
from flask_app.Controllers import AuthorController
from flask_app.Controllers import BookController

if __name__=='__main__':
    app.run(debug=True)