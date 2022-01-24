from flask import Flask, render_template, request, redirect
from user import Users
app = Flask(__name__)    

@app.route('/')
def home():
    return render_template('index.html', users=Users.get_all())

@app.route('/AddUser')
def addUser():
    return render_template('AddUser.html')

@app.route('/Insert', methods=['POST'])
def ReRoute():
    Users.save(request.form)
    return redirect('/')

@app.route('/User/<int:user_id>')
def Profile(user_id):
    return render_template('UserProfile.html', user=Users.get_one({'id':user_id}))

@app.route('/Edit/<int:user_id>')
def EditUser(user_id):
    return render_template('EditUser.html', user=Users.get_one({'id':user_id}))

@app.route('/update/<int:user_id>', methods=['POST'])
def SubmitEdit(user_id):
    updated_info = {
        **request.form,'id':user_id
    }
    Users.update(updated_info)
    return redirect(f'/User/{user_id}')

@app.route('/Delete/<int:user_id>')
def DeleteUser(user_id):
    Users.delete({'id':user_id})
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)