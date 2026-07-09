from flask import Flask, render_template, flash

app = Flask(__name__)

app.secret_key='12345678'

@app.route("/")
def hello_world():
    flash("Thank you", "Success")
    return render_template("index.html") 

app.run(debug=True)