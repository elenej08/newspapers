from flask import render_template
from exstension import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/box1')
def  box1():
    return render_template('box1.html')

@app.route('/box2')
def box2():
    return render_template('box2.html')

@app.route('/box3')
def box3():
    return render_template('box3.html')

























