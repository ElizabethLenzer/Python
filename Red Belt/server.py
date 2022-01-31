from flask_app import app
from flask_app.Controllers import Recipe_Controller
from flask_app.Controllers import User_Controller

if __name__=='__main__':
    app.run(debug=True)