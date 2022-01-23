from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def counter():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template('index.html',count=session['count'])

@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)