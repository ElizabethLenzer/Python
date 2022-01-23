from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', rows=8, columns=8, color1="red", color2="black")

@app.route('/<int:rows>')
def checkerboardRows(rows):
    return render_template('index.html', rows=rows, columns=8, color1="red", color2="black")

@app.route('/<int:rows>/<int:columns>')
def checkerboardRows(rows,columns):
    return render_template('index.html', rows=rows, columns=columns, color1="red", color2="black")

@app.route('/<int:rows>/<int:columns>/<string=color1>/<string=color2>')
def checkerboardRows(rows,columns,color1,color2):
    return render_template('index.html', rows=rows, columns=columns, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)