from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninjas.html')
def ninjasPage():
    return render_template('ninjas.html')

@app.route('/dojos.html')
def dojosPage():
    return render_template('dojos.html')



app.run(debug=True)
