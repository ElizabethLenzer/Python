from flask_app import app
from flask_app.Controllers import ninjas_Controller
from flask_app.Controllers import dojos_Controller

if __name__=='__main__':
    app.run(debug=True)