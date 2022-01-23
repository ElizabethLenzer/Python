from flask import Flask, render_template, session, request
app=Flask(__name__)
app.secret_key='I am top secret'

@app.route('/')
def Dojo():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def Result():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['fav']=request.form['fav']
    session['comment']=request.form['comment']
    return render_template('submitted.html')

if __name__=="__main__":
    app.run(debug=True)